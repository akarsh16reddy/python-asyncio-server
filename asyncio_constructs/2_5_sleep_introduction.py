import asyncio
from util import delay

async def hello_world_message() -> str:
    await asyncio.sleep(2)
    return "Hello World!"

async def main() -> None:
    message = await hello_world_message()
    print(message)

asyncio.run(main())
