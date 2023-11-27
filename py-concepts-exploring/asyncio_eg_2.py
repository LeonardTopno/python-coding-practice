# Important point to note: We need to take care of where you are awaiting the task.

import asyncio


async def main():
    task = asyncio.create_task(other_function())
    await task
    print("A")
    await asyncio.sleep(1)
    print("B")


async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")


if __name__ == "__main__":
    asyncio.run(main())

""" Output
1
wait for 2 sec
2
A
wait for 1 sec
B
------
Clearly we don't want this. This is again like a synchronous programming only.
"""