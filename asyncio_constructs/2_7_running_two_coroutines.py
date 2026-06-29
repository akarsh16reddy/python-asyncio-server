import asyncio
from util import delay

async def add_one(number: int) -> int:
    return number + 1

async def hello_world_message() -> str:
    await delay(5)
    return "Hello World"

async def main() -> None:
    message = await hello_world_message()
    one_plus_one = await add_one(1)

    print(one_plus_one)
    print(message)

asyncio.run(main()) # main() instead of main because it creates a coroutine object.
