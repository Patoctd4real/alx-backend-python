#!/usr/bin/env python3
'''taskz 0 Write an asynchronous coroutine.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Returns a random float between 0 and max_delay
    Args:
    '''
    merge = random.uniform(0, max_delay)
    await asyncio.sleep(merge)
    return merge
