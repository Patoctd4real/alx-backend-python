#!/usr/bin/env python3
'''Task 0' asynchronous coroutine.
'''
import asyncio
import random
async def wait_random(max_delay: int = 10) -> float:
    '''Waits for some second before random number.
    '''
    rand = random.random() * max_delay
    await asyncio.sleep(rand)
    return rand
