"""
Create multiple `tasks` from a `coroutine`
"""

import asyncio
from asyncio import Task 
from typing import List # to provide support for `type hints` # Optional, only for documentation

import logging

from coroutines import simple_coroutine # Importing our coroutine

async def create_tasks(num_tasks: int) -> List[Task]:  
    # In this context, `List` is a `type hint` provided by `typing` module
    # It indicates that a variable is expected to hold a list of elements.
    """
    Create n number of asyncio tasks to be executed.
    
    :param int num_tasks: Number of tasks to create.

    :return: List[Task]
    """

    task_list = []

    logging.info(f"Creating {num_tasks} tasks to be executed...")
    for i in range(num_tasks):
        task = asyncio.create_task(simple_coroutine(i), name=f"Task #{i}")
        task_list.append(task)
        logging.info(f"Created Task: {task}")
    return task_list



"""
`typing` Module: The `typing` module provides support for type hints.
Type hints are a way to indicate the expected type of a value in your code.
They're used primarily for documentation purposes and can be helpful for `Static Analysis Tools` like `linters` or `type checkers` 
"""


