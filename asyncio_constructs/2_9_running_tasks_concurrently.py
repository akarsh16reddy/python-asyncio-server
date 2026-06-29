import asyncio
from util import delay
import time

async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))
   
    # co-routines are async def, need invocation to create those objs
    # tasks are objects created through create_task

    # co-routines are sync await
    # tasks are async await
    start_time = time.time()
    await sleep_for_three
    await sleep_again
    await sleep_once_more
    end_time = time.time()
    
    print(f'Time taken: {end_time - start_time}')
    
asyncio.run(main())

# async def main():
#     sleep_for_three = delay(3)
#     sleep_again = delay(3)
#     sleep_once_more = delay(3)
#
#     # co-routines are async def, need invocation to create those objs
#     # tasks are objects created through create_task
#
#     # co-routines are sync await
#     # tasks are async await
#     start_time = time.time()
#     await sleep_for_three
#     await sleep_again
#     await sleep_once_more
#     end_time = time.time()
#
#     print(f'Time taken: {end_time - start_time}')
#
# asyncio.run(main())
