#!/usr/bin/env python3
'''Task 0.3 return a tasks' 
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''wait_random that takes an int returns asyncio.Task
    '''
    return asyncio.create_task(wait_random(max_delay))
