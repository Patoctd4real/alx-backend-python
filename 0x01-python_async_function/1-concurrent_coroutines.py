#!/usr/bin/env python3
'''Task 0.1 executing multiple coroutines @ the same time with async'
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''time it wait to convert random.
    '''
    merge = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(merge)
