import asyncio

from util import delay

# OUTPUT:
# Sleeping for 3 second(s)
# Sleeping for 1 second(s)
# Finished sleeping for 1 second(s)
# Finished sleeping for 3 second(s)
# [3, 1]


async def main():
    results = await asyncio.gather(delay(3), delay(1))
    print(results)


asyncio.run(main())
