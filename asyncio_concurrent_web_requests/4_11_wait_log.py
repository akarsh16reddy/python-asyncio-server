import asyncio
import logging

import aiohttp
from aiohttp import ClientSession

from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        good_request = asyncio.create_task(
            fetch_status(session, "https://www.example.com")
        )

        bad_request = asyncio.create_task(
            fetch_status(session, "python://www.example.com")
        )

        fetchers = [good_request, bad_request]
        done, pending = await asyncio.wait(fetchers)

        print(f"Done task count: {len(done)}")
        print(f"Pending task count: {len(pending)}")

        for done_task in done:
            # result = await done_task  # this will throw an exception
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("Request got exception", exc_info=done_task.exception())


asyncio.run(main())
