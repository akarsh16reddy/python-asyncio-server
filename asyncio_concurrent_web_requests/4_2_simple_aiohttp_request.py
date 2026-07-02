import asyncio

import aiohttp
from aiohttp import ClientSession

from util import async_timed, fetch_status


@async_timed()
async def fetch_status_code(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://www.example.com"
        status: int = await fetch_status(session, url)
        print(f"Status for {url} was {status}")


asyncio.run(main())
