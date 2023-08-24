# import json
# from collections.abc import Iterable
#
# from urllib import robotparser
# from urllib.parse import urljoin, urlparse
#
# from aioredis import Redis
# from bs4 import BeautifulSoup
# import asyncio
# from typing import Awaitable, Callable
# import aiohttp
# import tenacity
# from aiohttp import BasicAuth
# from aiohttp.client import _RequestContextManager, ClientTimeout
# from aiohttp.typedefs import LooseCookies, LooseHeaders
# from tenacity import AsyncRetrying, stop_after_attempt, wait_fixed
# import aioredis
# import logging
# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG)
#
#
# class SafeAsyncSession(aiohttp.ClientSession):
#     """SafeAsyncSession class to send async requests in datasource clients."""
#
#     DEFAULT_SEMAPHORES = 50
#     DEFAULT_ATTEMPTS = 2
#     DEFAULT_WAIT_SECONDS = 1
#     DEFAULT_USER_AGENT = "SelfLearningCrawlerName/1.0 (+https://example.com/)"
#     DEFAULT_TIMEOUT = 5
#
#     def __init__(
#         self,
#         semaphore: int = DEFAULT_SEMAPHORES,
#         auth: BasicAuth = None,
#         headers: LooseHeaders = None,
#         cookies: LooseCookies = None,
#         max_attempts: tenacity.stop = None,
#         wait: tenacity.wait = None,
#     ) -> None:
#         """Init method with added semaphore parameter."""
#         timeout = ClientTimeout(total=self.DEFAULT_TIMEOUT)
#         super().__init__(auth=auth, headers=headers, cookies=cookies, timeout=timeout)
#         self.semaphore = asyncio.Semaphore(semaphore)
#         self.max_attempts = max_attempts if max_attempts else stop_after_attempt(self.DEFAULT_ATTEMPTS)
#         self.wait = wait if wait else wait_fixed(self.DEFAULT_WAIT_SECONDS)
#         self.headers.setdefault('User-Agent', self.DEFAULT_USER_AGENT)
#
#     async def get(self, url: str, raise_for_status: bool = True, **kwargs) -> Awaitable:
#         """Send async get request with parameters."""
#         logger.debug(f"GET: {url}, kwargs: {kwargs}.")
#         return await self.exec_with_retry(
#             lambda: super(SafeAsyncSession, self).get(
#                 url=url, **kwargs, raise_for_status=raise_for_status, allow_redirects=True
#             )
#         )
#
#     async def exec_with_retry(self, func: Callable) -> _RequestContextManager | None:
#         """Execute method with retries."""
#         async with self.semaphore:
#             async for attempt in AsyncRetrying(stop=self.max_attempts, wait=self.wait, reraise=True):
#                 with attempt:
#                     return await func()
#         return None
#
#
# class RobotsHandler:
#     def __init__(self, session):
#         self.parsers = {}
#         self.session = session
#
#     def can_fetch(self, url, user_agent=None):
#         if not user_agent:
#             user_agent = self.session.headers.get('User-Agent', '*')
#         parsed_url = urlparse(url)
#         return self.parsers[parsed_url.netloc].can_fetch(useragent=user_agent, url=parsed_url.path)
#
#     async def fetch_robots_for_urls(self, urls: Iterable):
#         domains = set((urlparse(url).netloc for url in urls))
#         return await asyncio.gather(
#             *(
#                 self.fetch_robots_file(domain) for domain in domains
#                 if domain not in self.parsers
#             )
#         )
#
#     async def fetch_robots_file(self, domain):
#         robots_url = f'https://{domain}/robots.txt'
#         try:
#             response = await self.session.get(robots_url)
#             response.raise_for_status()
#             text = await response.text()
#             lines = text.splitlines()
#             logger.info(f'Successfully fetched robots.txt. Domain {domain}')
#         except Exception as e:
#             logger.error(f'Failed to fetch robots.txt for {domain}. {str(e)}')
#             lines = []
#         parser = robotparser.RobotFileParser()
#         parser.parse(lines)
#         self.parsers[domain] = parser
#
#
# class Crawler:
#     """Crawler class. Main execution class for web crawling."""
#
#     def __init__(self, seed_url, max_depth, search_word, semaphore=30):
#         """Init method."""
#         self.seed_url = seed_url
#         self.max_depth = max_depth
#         self.search_word = search_word.strip().lower()
#         self.visited_urls = set()
#         self.queue = [(seed_url, 0)]
#         self.word_count = 0
#         self.semaphore = semaphore
#
#     async def crawl(self):
#         async with SafeAsyncSession(semaphore=self.semaphore) as session:
#             robots_handler = RobotsHandler(session)
#             while self.queue:
#                 tasks = await self.init_async_tasks(session, robots_handler)
#                 data = await asyncio.gather(*tasks, return_exceptions=True)
#                 await self.process_data_and_update_queue(data)
#         return self.word_count
#
#     async def init_async_tasks(self, session, robots_handler) -> list:
#         self.visited_urls.update((url for url, _ in self.queue))
#         await robots_handler.fetch_robots_for_urls((url for url, _ in self.queue))
#         tasks = []
#         for url, depth in self.queue:
#             if not robots_handler.can_fetch(url):
#                 logger.info(f'Skipped fetching due to robots.txt restrictions. {url}')
#                 continue
#             url_processor = URLProcessor(session, url, self.search_word, depth)
#             tasks.append(url_processor.process_web_page())
#         self.queue.clear()
#         return tasks
#
#     async def add_links_to_the_queue(self, links, next_depth):
#         for link in links:
#             if link in self.visited_urls:
#                 continue
#             self.queue.append((link, next_depth))
#
#     async def process_data_and_update_queue(self, data):
#         for item in data:
#             if isinstance(item, Exception):
#                 logger.error(f'Error during task: {str(item)}')
#                 continue
#             links, count, next_depth = item
#             self.word_count += count
#             if next_depth == self.max_depth:
#                 continue
#             await self.add_links_to_the_queue(links, next_depth)
#
#
# class URLProcessor:
#     def __init__(self, session, url, search_word, depth):
#         self.session = session
#         self.url = url
#         self.search_word = search_word
#         self.depth = depth
#
#     async def fetch(self) -> str | None:
#         response = await self.session.get(self.url)
#         return await response.text()
#
#     async def process_web_page(self):
#         text = await self.fetch()
#         soup = BeautifulSoup(text, 'lxml')
#         # Extracting text from only <p> tags
#         text = ' '.join(p.get_text() for p in soup.find_all(('p',)))
#         word_count = text.lower().count(self.search_word)
#         links = self.find_next_depth_links(soup)
#         logger.info(f'{self.url}, {word_count}, {self.depth}')
#         return links, word_count, self.depth + 1
#
#     def find_next_depth_links(self, soup):
#         links = set(
#             (
#                 urljoin(self.url, a['href']) for a in soup.find_all('a', href=True)
#                 if URLUtility.is_relevant_url(urljoin(self.url, a['href']))
#             )
#         )
#         return links
#
#
# class URLUtility:
#
#     @staticmethod
#     def is_relevant_url(url):
#         parsed_url = urlparse(url)
#         if parsed_url.path:
#             ext = parsed_url.path.split('.')[-1]
#             if ext in {"jpg", "jpeg", "png", "gif", "pdf"}:
#                 return False
#         return True
#
#
# if __name__ == '__main__':
#     crawler = Crawler(
#         seed_url='https://en.wikipedia.org',
#         max_depth=2,
#         search_word='english'
#     )
#     asyncio.run(crawler.crawl())
#     print(crawler.word_count)
