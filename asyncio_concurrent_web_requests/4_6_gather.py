import asyncio

import aiohttp
from aiohttp import ClientSession

from util import async_timed, delay, fetch_status


@async_timed()
async def with_gather():  # asynchronous
    async with ClientSession() as session:
        urls = ["https://www.example.com" for _ in range(10)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


@async_timed()
async def without_gather():  # synchronous
    async with ClientSession() as session:
        urls = ["https://www.example.com" for _ in range(10)]
        status_codes = [await fetch_status(session, url) for url in urls]
        print(status_codes)


async def main():
    await without_gather()
    await with_gather()


asyncio.run(main())
