import asyncio
from asyncio import Future

async def main():
    my_future = Future()
    
    print(f'Is my_future done? {my_future.done()}')
    
    my_future.set_result(42)
    
    print(f'Is my_future done? {my_future.done()}')
    print(f'What is the result of my_future? {my_future.result()}') # .result throws exception if not set

asyncio.run(main())
