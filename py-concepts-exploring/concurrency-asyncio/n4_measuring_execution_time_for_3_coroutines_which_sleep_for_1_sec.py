"""
Tracking Execution Time of 3 coroutines which sleeps for 1 sec each
"""

import asyncio

from .n1_coroutines import simple_coroutine  # Importing our coroutine


async def main():
    await asyncio.gather(simple_coroutine(1), simple_coroutine(2), simple_coroutine(3))


if __name__ == "__main__":  # this has to do with file and not with the function main() (a courintine) defined above
    import time

    start_time = time.perf_counter()
    asyncio.run(main())
    print(f"Executed {__name__} in {time.perf_counter() - start_time : 0.2f} seconds")

"""
Output:
    Coroutine 1 has finished executing.
    Coroutine 2 has finished executing.
    Coroutine 3 has finished executing.
    Executed __main__ in  1.00 seconds
"""

""" Leo's Note
What else to learn from this program
i) How to code to to execution time of a function (time taken by a function to complete)
ii)  
"""
