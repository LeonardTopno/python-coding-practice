# In order to actually  do programming asynchronously with async we need to work with task
import asyncio


async def main():
    task = asyncio.create_task(other_function())  # The task is now scheduled
    print("A")                                    # Once we have some idle time, we are going to call that task
    await asyncio.sleep(1)
    print("B")
    await task


async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")

asyncio.run(main())
