import asyncio
import signal
from asyncio import AbstractEventLoop
from typing import Set

from util import delay


# Only works on Unix-like machines
def cancel_tasks():
    print("Received a SIGINT")
    tasks = asyncio.all_tasks()  # ignore: type: Set[asyncio.Task]
    print(f"Cancelling {len(tasks)} task(s).")
    [task.cancel() for task in tasks]


async def main():
    loop: AbstractEventLoop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, cancel_tasks)

    _ = await delay(10)


asyncio.run(main())
