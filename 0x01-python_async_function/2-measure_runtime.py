#!/usr/bin/env python3
'''Task 0.2 Measuring the runing time' 
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''execute the elapsed time of wait_n.
    '''
    show_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - show_time) / n
