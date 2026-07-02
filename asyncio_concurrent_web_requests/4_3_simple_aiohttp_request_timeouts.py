import asyncio

import aiohttp
from aiohttp import ClientSession

from util import async_timed, fetch_status


@async_timed()
async def fetch_status_code(session: ClientSession, url: str) -> int:
    request_time_out = aiohttp.ClientTimeout(total=0.5)
    async with session.get(url, timeout=request_time_out) as result:
        return result.status


async def main():
    client_timeout = aiohttp.ClientTimeout(total=1, connect=0.2)
    async with aiohttp.ClientSession(timeout=client_timeout) as session:
        url = "https://www.example.com"
        status: int = await fetch_status_code(session, url)
        print(f"Status for {url} was {status}")


asyncio.run(main())
