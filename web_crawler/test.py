from urllib import robotparser
from urllib.parse import urljoin, urlparse
import json
from uuid import uuid4

from bs4 import BeautifulSoup
import asyncio
from typing import Awaitable, Callable
import aiohttp
from redis.asyncio import Redis
import tenacity
from aiohttp import BasicAuth
from aiohttp.client import _RequestContextManager, ClientTimeout
from aiohttp.typedefs import LooseCookies, LooseHeaders
from tenacity import AsyncRetrying, stop_after_attempt, wait_fixed
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class SafeAsyncSession(aiohttp.ClientSession):
    """SafeAsyncSession class to send async requests in datasource clients."""

    DEFAULT_SEMAPHORES = 50
    DEFAULT_ATTEMPTS = 2
    DEFAULT_WAIT_SECONDS = 1
    DEFAULT_USER_AGENT = "SelfLearningCrawlerName/1.0 (+https://example.com/)"
    DEFAULT_TIMEOUT = 5

    def __init__(
        self,
        semaphore: int = DEFAULT_SEMAPHORES,
        auth: BasicAuth = None,
        headers: LooseHeaders = None,
        cookies: LooseCookies = None,
        max_attempts: tenacity.stop = None,
        wait: tenacity.wait = None,
    ) -> None:
        """Init method with added semaphore parameter."""
        timeout = ClientTimeout(total=self.DEFAULT_TIMEOUT)
        super().__init__(auth=auth, headers=headers, cookies=cookies, timeout=timeout)
        self.semaphore = asyncio.Semaphore(semaphore)
        self.max_attempts = max_attempts if max_attempts else stop_after_attempt(self.DEFAULT_ATTEMPTS)
        self.wait = wait if wait else wait_fixed(self.DEFAULT_WAIT_SECONDS)
        self.headers.setdefault('User-Agent', self.DEFAULT_USER_AGENT)

    async def get(self, url: str, raise_for_status: bool = True, **kwargs) -> Awaitable:
        """Send async get request with parameters."""
        # logger.debug(f"GET: {url}, kwargs: {kwargs}.")
        return await self.exec_with_retry(
            lambda: super(SafeAsyncSession, self).get(
                url=url, **kwargs, raise_for_status=raise_for_status, allow_redirects=True
            )
        )

    async def exec_with_retry(self, func: Callable) -> _RequestContextManager | None:
        """Execute method with retries."""
        async with self.semaphore:
            async for attempt in AsyncRetrying(stop=self.max_attempts, wait=self.wait, reraise=True):
                with attempt:
                    return await func()
        return None


class RobotsHandler:
    def __init__(self, session, redis):
        self.parsers = {}
        self.session = session
        self.redis: Redis = redis

    def can_fetch(self, url, user_agent=None):
        if not user_agent:
            user_agent = self.session.headers.get('User-Agent', '*')
        parsed_url = urlparse(url)
        result = self.parsers[parsed_url.netloc].can_fetch(useragent=user_agent, url=parsed_url.path)
        return result

    async def fetch_robots_file(self, domain):
        robots_url = f'https://{domain}/robots.txt'
        try:
            response = await self.session.get(robots_url)
            response.raise_for_status()
            text = await response.text()
            lines = text.splitlines()
            logger.info(f'Successfully fetched robots.txt. Domain {domain}')
        except Exception as e:
            logger.error(f'Failed to fetch robots.txt for {domain}. {str(e)}')
            lines = []
        parser = robotparser.RobotFileParser()
        parser.parse(lines)
        self.parsers[domain] = parser


class Crawler:
    """Crawler class. Main execution class for web crawling."""

    domain_set = 'domain_set'
    visited = 'visited'

    def __init__(self, seed_url, max_depth, search_word, semaphore=30):
        """Init method."""
        self.seed_url = seed_url
        self.max_depth = max_depth
        self.search_word = search_word.strip().lower()
        self.word_count = 0
        self.semaphore = semaphore
        self.redis = Redis(password='test_password', decode_responses=True)

    async def init_redis(self):
        domain = urlparse(self.seed_url).netloc
        await self.redis.sadd(self.visited, self.seed_url)
        await self.redis.sadd(self.domain_set, domain)
        await self.redis.rpush(f'domain_queue:{domain}', json.dumps({'url': self.seed_url, 'depth': 0}))

    async def clean_redis(self):
        await self.redis.flushdb(asynchronous=True)

    async def crawl(self):
        await self.init_redis()
        async with SafeAsyncSession(semaphore=self.semaphore) as session:
            robots_handler = RobotsHandler(session, self.redis)
            while True:
                domains = await self.redis.smembers(self.domain_set)
                if not domains:
                    break
                await self.redis.delete(self.domain_set)
                tasks = (self.worker(domain, session, robots_handler) for domain in domains)
                await asyncio.gather(*tasks, return_exceptions=True)
        await self.clean_redis()
        await self.redis.close()
        return self.word_count

    async def worker(self, domain, session, robots_handler):
        if domain not in robots_handler.parsers:
            domain_locked = await self.redis.setnx(f'domain_lock:{domain}', 1)
            if not domain_locked:
                return
            # successfully locked domain
            await robots_handler.fetch_robots_file(domain)
            await self.redis.delete(f'domain_lock:{domain}')
        urls = await self.redis.lrange(f'domain_queue:{domain}', 0, -1)
        if not urls:
            return
        urls = (json.loads(i) for i in urls)
        tasks = (
            self.process_url(session, i['url'], i['depth'])
            for i in urls if robots_handler.can_fetch(i['url'])
        )
        result = await asyncio.gather(*tasks)

        new_tasks = []
        for links, word_count, next_depth in result:
            self.word_count += word_count
            if next_depth == self.max_depth:
                continue
            new_tasks.append(self.enqueue_batch(links, next_depth))
        await asyncio.gather(*new_tasks)

    async def process_url(self, session, url, depth):
        url_processor = URLProcessor(session, url, self.search_word, depth)
        return await url_processor.process_web_page()

    async def enqueue_batch(self, links: set, next_depth: int):
        temp_set_name = f'links_set_{uuid4().hex}'
        await self.redis.sadd(temp_set_name, *links)
        new_links = await self.redis.sdiff(keys=[temp_set_name, self.visited])
        await self.redis.delete(temp_set_name)
        if not new_links:
            return
        await self.redis.sadd(self.visited, *new_links)
        domain_links_map = {}
        for link in new_links:
            domain = urlparse(link).netloc
            if domain not in domain_links_map:
                domain_links_map[domain] = []
            domain_links_map[domain].append(json.dumps({'url': link, 'depth': next_depth}))
        tasks = [self.domain_batch_insert(domain, links) for domain, links in domain_links_map.items()]
        await asyncio.gather(*tasks)

    async def domain_batch_insert(self, domain, links):
        await self.redis.rpush(f'domain_queue:{domain}', *links)
        await self.redis.sadd(self.domain_set, domain)


class URLProcessor:
    def __init__(self, session, url, search_word, depth):
        self.session = session
        self.url = url
        self.search_word = search_word
        self.depth = depth

    async def fetch(self) -> str | None:
        response = await self.session.get(self.url)
        return await response.text()

    async def process_web_page(self):
        text = await self.fetch()
        soup = BeautifulSoup(text, 'lxml')
        # Extracting text from only <p> tags
        text = ' '.join(p.get_text() for p in soup.find_all(('p',)))
        word_count = text.lower().count(self.search_word)
        links = self.find_next_depth_links(soup)
        logger.info(f'{self.url}, {word_count}, {self.depth}')
        return links, word_count, self.depth + 1

    def find_next_depth_links(self, soup):
        links = set(
            (
                urljoin(self.url, a['href']) for a in soup.find_all('a', href=True)
                if URLUtility.is_relevant_url(urljoin(self.url, a['href']))
            )
        )
        return links


class URLUtility:

    @staticmethod
    def is_relevant_url(url):
        parsed_url = urlparse(url)
        if parsed_url.path:
            ext = parsed_url.path.split('.')[-1]
            if ext in {"jpg", "jpeg", "png", "gif", "pdf"}:
                return False
        return True


if __name__ == '__main__':
    crawler = Crawler(
        seed_url='https://en.wikipedia.org',
        max_depth=2,
        search_word='english'
    )
    asyncio.run(crawler.crawl())
    print(crawler.word_count)
