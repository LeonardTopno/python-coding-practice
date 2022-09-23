import asyncio
import time

counter=0

async def func1():
    global counter

    while True:
        counter+=1
        counter-=1
        print("func1: ", counter)

        await asyncio.sleep(0)

async def func2():

    global counter

    while True:
        counter+=1
        counter-=1
        print("func2: ", counter)

        await asyncio.sleep(0)

asyncio.gather(func1(), func2())
asyncio.get_event_loop().run_forever()