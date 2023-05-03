#!/usr/bin/env python3
'''Task 0.0 Async Generator.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''To loop through 10 numbers.
    '''
    for x in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
