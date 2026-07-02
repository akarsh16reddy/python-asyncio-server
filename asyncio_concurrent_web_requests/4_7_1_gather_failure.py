import asyncio

import aiohttp
from aiohttp import ClientSession

from util import async_timed, delay, fetch_status


@async_timed()
async def with_gather():  # asynchronous
    async with ClientSession() as session:
        urls = ["python://www.example.com", "https://www.example.com"]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


@async_timed()
async def with_gather_return_exceptions():  # asynchronous
    async with ClientSession() as session:
        urls = ["python://www.example.com", "https://www.example.com"]
        requests = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*requests, return_exceptions=True)
        exceptions = list(filter(lambda x: isinstance(x, Exception), results))
        success = list(filter(lambda x: not isinstance(x, Exception), results))
        print(f"All results {results}")
        print(f"Exceptions: {exceptions}")
        print(f"success: {success}")


async def main():
    await with_gather_return_exceptions()


asyncio.run(main())
