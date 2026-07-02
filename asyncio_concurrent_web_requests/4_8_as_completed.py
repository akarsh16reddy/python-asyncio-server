import asyncio

import aiohttp
from aiohttp import ClientSession

from util import async_timed, fetch_status

# as_completed is not blocking in the sense that its __next__() runs
# synchronously. But more importantly, it never hands you a specific task
# But more importantly, it never hands you a specific task
# to wait on — each wrapper it yields says "wait for whichever task
# finishes next."
#
# Think of it like a race finish line:
#
# as_completed sets up 3 runners and hands you 3 "tickets."
# Each ticket says: "await me → get the NEXT runner to cross the finish
# line."
# It does NOT say: "await me → get runner #3."
#
# So your scenario — "what if it gives me the 10-second task first?" —
# can't happen. The wrappers aren't pre-assigned to specific tasks.
# Internally:
#
#               ┌─ Task 1 (1s) ──── callback → queue.append(Task1) ──┐
#               ├─ Task 2 (1s) ──── callback → queue.append(Task2) ──┤
#               └─ Task 3 (10s) ─── callback (hasn't fired yet) ─────┘
#
# Wrapper #1: await → popleft() from queue → gets Task1 (1st to finish)
# Wrapper #2: await → popleft() from queue → gets Task2 (already there)
# Wrapper #3: await → queue empty → WAIT → callback fires → gets Task3
#
# The queue enforces completion order automatically. A task only enters the
# queue when its done callback fires, and callbacks fire in the order
# tasks finish. The 10-second task's callback simply hasn't fired yet at
# T=1s, so it can't possibly be handed to an early wrapper.
#
# So: as_completed itself doesn't block, and await finished_task only
# blocks until the next task finishes — which is always the fastest
# remaining one, never a specific slow one.


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        example_fetcher = lambda t: fetch_status(session, "https://www.example.com", t)
        fetchers = map(example_fetcher, [1, 1, 10])
        for finished_task in asyncio.as_completed(
            fetchers
        ):  # I guess this yields each task as they finish
            result = await finished_task
            print(result)


asyncio.run(main())
