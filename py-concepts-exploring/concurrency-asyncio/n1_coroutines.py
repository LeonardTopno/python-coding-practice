"""
Defining a Coroutine function to be executed asynchronously.
This is to understand what actullay is a coroutine.
"""

import asyncio

import logging

async def simple_coroutine(number: int):
    """
    Wait for a time delay and & display number associted with the coroutine.

    :parma int number: Number to identify current coroutine
    """
    await asyncio.sleep(1)
    print(f"Coroutine {number} has finished executing.")
    logging.info(f"Coroutine {number} has finished executing.") 
    


""""
Notes:
simple_coroutine() halts its execution for 1 second before logging a message.
Coroutines can't be involked like regular functions;
attempting to run simple_coroutine(1) won't work unless it's run inside an 'asyncio event loop'. 

Functions to know
asyncio.run(main())
await asyncio.sleep(1)
await asyncio.gather(coroutine_1, coroutine_2, coroutine_3)


""" 
