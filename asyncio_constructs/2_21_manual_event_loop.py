import asyncio
import requests
from util import delay, async_timed

async def main():
    await asyncio.sleep(1)
    print('Printing after 1 second from main()')

loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()
