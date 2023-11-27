# Doing Synchronous Programming Using Asynchronous Functions
import asyncio


async def main():
    print("A")
    await other_function()
    print("B")


async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")

if __name__ == "__main__":
    asyncio.run(main())


""" Output
A
1
2
B
"""
