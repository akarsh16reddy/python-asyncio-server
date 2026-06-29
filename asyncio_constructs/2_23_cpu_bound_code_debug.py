import asyncio
from util import async_timed, delay

@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for _ in range(100000000):
        counter += 1
    return counter

# @async_timed()
async def main():
    task_one = asyncio.create_task(cpu_bound_work())


async def main():
    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = 5 # changes acceptable time limit
    task_one = asyncio.create_task(cpu_bound_work())

asyncio.run(main(), debug=True)
