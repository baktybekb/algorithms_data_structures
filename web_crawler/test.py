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

    async def acquire_lock(self, domain):
        lock_name = f'lock:{domain}'
        locked = await self.redis.set(lock_name, 1, ex=10, nx=True)
        return locked

    async def release_lock(self, domain):
        lock_name = f'lock:{domain}'
        await self.redis.delete(lock_name)

    async def fetch_robots_file(self, domain, url, depth):
        robots_url = f'https://{domain}/robots.txt'
        have_set = await self.acquire_lock(domain)
        if not have_set:
            await asyncio.sleep(0.1)
            await self.redis.rpush('queue', json.dumps({'url': url, 'depth': depth}))
            return
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
        await self.release_lock(domain)
        return True


class Crawler:
    """Crawler class. Main execution class for web crawling."""

    QUEUE = 'queue'
    VISITED = 'visited'

    def __init__(self, seed_url, max_depth, search_word, semaphore=30):
        """Init method."""
        self.seed_url = seed_url
        self.max_depth = max_depth
        self.search_word = search_word.strip().lower()
        self.word_count = 0
        self.semaphore = semaphore
        self.redis = Redis(password='test_password', decode_responses=True)

    async def init_redis(self):
        await self.redis.sadd(self.VISITED, self.seed_url)
        await self.redis.rpush(self.QUEUE, json.dumps({'url': self.seed_url, 'depth': 0}))

    async def clean_redis(self):
        await self.redis.delete(self.VISITED, self.QUEUE)

    async def crawl(self):
        await self.init_redis()
        async with SafeAsyncSession(semaphore=self.semaphore) as session:
            robots_handler = RobotsHandler(session, self.redis)
            data = json.loads(await self.redis.lpop(self.QUEUE))
            await self.process_url(session, data['url'], data['depth'])
            tasks = (self.new_worker(robots_handler, session) for _ in range(self.semaphore))
            await asyncio.gather(*tasks, return_exceptions=True)
        await self.clean_redis()
        await self.redis.close()
        return self.word_count

    async def new_worker(self, robots_handler, session):
        while True:
            data = await self.redis.lpop(self.QUEUE, self.semaphore)
            if not data:
                break
            data = (json.loads(i) for i in data)
            tasks = (self.helper(session, i['depth'], i['url'], robots_handler) for i in data)
            await asyncio.gather(*tasks, return_exceptions=True)

    async def helper(self, session, depth, url, robots_handler):
        domain = urlparse(url).netloc
        if domain not in robots_handler.parsers:
            fetched = await robots_handler.fetch_robots_file(domain, url, depth)
            if not fetched:
                return
        if not robots_handler.can_fetch(url):
            logger.info(f'skipped fetching due to robots.txt restrictions. {url}')
            return
        await self.process_url(session, url, depth)

    async def process_url(self, session, url, depth):
        url_processor = URLProcessor(session, url, self.search_word, depth)
        links, word_count, next_depth = await url_processor.process_web_page()
        self.word_count += word_count
        if next_depth == self.max_depth:
            return
        await self.enqueue_batch(links, next_depth)

    async def enqueue_batch(self, links: set, next_depth: int):
        temp_set_name = f'links_set_{uuid4().hex}'
        await self.redis.sadd(temp_set_name, *links)
        new_links = await self.redis.sdiff(keys=[temp_set_name, self.VISITED])
        await self.redis.delete(temp_set_name)
        if not new_links:
            return
        await self.redis.sadd(self.VISITED, *new_links)
        await self.redis.rpush(self.QUEUE, *(json.dumps({'url': link, 'depth': next_depth}) for link in new_links))


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
