"""
Running 3 coroutines inside an EVENT LOOP
Purpose: How to define an EVENT LOOP and how to put coroutines inside it

asyncio.gather()
i) The asyncio.gather() is a function provided by Python asyncio library that allows multiple coroutines to be exeuted concurrently
and wait for all of them to comeplete before continuing.


ii) The asyncio.gather() function runs multiple asynchronous operations, wraps a coroutine as a task, and returns a tuple of result in the saem order of AWAITBALES.

iii) Set 'return_expectations' to 'True' to allow erros to be returned as results

"""

import asyncio 

from coroutines import simple_coroutine # Import our coroutine (function)


async def main():
    await asyncio.gather(simple_coroutine(1), simple_coroutine(2), simple_coroutine(3))

if __name__ == "__main__":
    asyncio.run(main())
