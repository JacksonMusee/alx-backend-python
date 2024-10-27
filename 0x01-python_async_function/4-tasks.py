#!/usr/bin/env python3
'''
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called
'''

import asyncio
from typing import List, Callable

task_wait_random: Callable = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Does as required above
    '''
    tasks = [task_wait_random(max_delay) for _ in range(0, n)]

    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
