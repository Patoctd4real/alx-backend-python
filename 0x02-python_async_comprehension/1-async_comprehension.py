#!/usr/bin/env python3
'''Task 0.1 Run time for four parallel comprehensions.
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''creating a ist of 10 generated numbers.
    '''
    return [x async for x in async_generator()]
