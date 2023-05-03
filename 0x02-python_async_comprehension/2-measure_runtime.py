#!/usr/bin/env python3
'''Task 2's module.
'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure and execute total time, comprehension 4 times
    '''
    show_time = time.time()
    await asyncio.gather(*(async_comprehension() for x in range(4)))
    return time.time() - show_time
