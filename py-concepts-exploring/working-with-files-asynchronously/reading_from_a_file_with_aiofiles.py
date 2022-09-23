"""
Reading from a file with aiofiles
"""

import aiofiles
import asyncio
import json
from pprint import pprint


# Open a file corresponding to a particular Pokemon, parsing its JSON into a dictionary, and printing out its name:
async def main():
    async with aiofiles.open('articuno.json', mode='r') as f:
        contents = await f.read()
    pokemon = json.loads(contents)
    print(pokemon.get("name"))  # print(pokemon["name"]) # Leo: Better to use .get() of dictionary
    pprint(pokemon)


# One can iterate through the file asynchronously, line by line
async def main1():
    async with aiofiles.open('articuno.json', mode='r') as f:
        async for line in f:
            print(line)


# Writing to a file with aiofiles
async def main2():
    # Read the contents of json file.
    async with aiofiles.open('rhydon.json', mode='r') as f:
        contents = await f.read()

    # Load it into a dictionary and create a list of moves.
    pokemon = json.loads(contents)
    name = pokemon.get("name")
    print(f"Name is: {name}")      # Leo: print("Name is:" name)
    # moves = [move["move"]["name"] for move in pokemon["moves"]]
    moves = [move.get("move").get("name") for move in pokemon.get("moves")]

    # Open a new file to write the list of moves into.
    async with aiofiles.open(f"{name}_moves.txt", mode="w") as f:
        print("\n".join(moves))
        await f.write("\n".join(moves))


asyncio.run(main2())

