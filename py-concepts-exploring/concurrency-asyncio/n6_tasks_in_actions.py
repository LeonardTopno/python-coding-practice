import asyncio
from n5_tasks import create_tasks


async def async_tasks_example():
    """
    Create and inspect tasks to wrap  simple functions.
    """
    task_list = await create_tasks(5)
    done, pending = await asyncio.wait(task_list)

    if done:
        print(f"{len(done)} tasks completed: {[task.get_name() for task in done]}.")

    if pending:
        print(f"{len(pending)} tasks pending: {[task.get_name() for task in pending]}.")

if __name__ == "__main__":
    asyncio.run(async_tasks_example())


""""   
Output: 
    Creating 5 tasks to be executed...
    Created Task: <Task pending name='Task #0' coro=<simple_coroutine() running at /Users/leo/LeoWorkSpace/python-coding-practice/py-concepts-exploring/concurrency-asyncio/n1_coroutines.py:11>>
    Created Task: <Task pending name='Task #1' coro=<simple_coroutine() running at /Users/leo/LeoWorkSpace/python-coding-practice/py-concepts-exploring/concurrency-asyncio/n1_coroutines.py:11>>
    Created Task: <Task pending name='Task #2' coro=<simple_coroutine() running at /Users/leo/LeoWorkSpace/python-coding-practice/py-concepts-exploring/concurrency-asyncio/n1_coroutines.py:11>>
    Created Task: <Task pending name='Task #3' coro=<simple_coroutine() running at /Users/leo/LeoWorkSpace/python-coding-practice/py-concepts-exploring/concurrency-asyncio/n1_coroutines.py:11>>
    Created Task: <Task pending name='Task #4' coro=<simple_coroutine() running at /Users/leo/LeoWorkSpace/python-coding-practice/py-concepts-exploring/concurrency-asyncio/n1_coroutines.py:11>>
    Coroutine 0 has finished executing.
    Coroutine 1 has finished executing.
    Coroutine 2 has finished executing.
    Coroutine 3 has finished executing.
    Coroutine 4 has finished executing.
    5 tasks completed: ['Task #3', 'Task #1', 'Task #0', 'Task #2', 'Task #4'].
"""