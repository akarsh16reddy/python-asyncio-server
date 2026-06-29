import asyncio
from util import delay

async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    # important: await triggers an iteration of the event loop
    result = await sleep_for_three
    print(result)

asyncio.run(main())
