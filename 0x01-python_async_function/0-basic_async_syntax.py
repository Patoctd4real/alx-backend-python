#!/usr/bin/env python3
'''Task 0' my module tasks.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for some second before random number.
    '''
    show_time = random.random() * max_delay
    await asyncio.sleep(show_time)
    return show_time
