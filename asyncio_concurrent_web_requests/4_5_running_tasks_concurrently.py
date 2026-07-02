import asyncio

from util import async_timed, delay


@async_timed()
async def parallel():
    delay_times = [3, 3, 3]
    tasks = [asyncio.create_task(delay(seconds)) for seconds in delay_times]
    [await task for task in tasks]


@async_timed()
async def sequential():
    delay_times = [3, 3, 3]
    # awaiting as soon as task is created - PROBLEM!
    _ = [await asyncio.create_task(delay(seconds)) for seconds in delay_times]


async def main():
    print("running sequential...")
    await sequential()
    print("running parallel...")
    await parallel()


asyncio.run(main())
