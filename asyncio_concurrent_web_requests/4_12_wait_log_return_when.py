import asyncio
import logging

import aiohttp
from aiohttp import ClientSession

from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, "python://www.badexample.com")),
            asyncio.create_task(
                fetch_status(session, "https://www.example.com", delay=3)
            ),
            asyncio.create_task(
                fetch_status(session, "https://www.example.com", delay=3)
            ),
        ]

        done, pending = await asyncio.wait(
            fetchers, return_when=asyncio.FIRST_EXCEPTION
        )

        print(f"Done task count: {len(done)}")
        print(f"Pending task count: {len(pending)}")

        for done_task in done:
            # result = await done_task  # this will throw an exception
            if done_task.exception() is None:
                print(done_task.result())
            else:
                # logging.error("Request got exception", exc_info=done_task.exception())
                pass

        print("Cancelling pending tasks:")
        for pending_task in pending:
            pending_task.cancel()


asyncio.run(main())
