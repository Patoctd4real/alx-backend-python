#!/usr/bin/env python3
""" task0.0 basics of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that takes in an integer argument
    """
    marge = random.uniform(0, max_delay)
    await asyncio.sleep(marge)
    return marge
