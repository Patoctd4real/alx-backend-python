#!/usr/bin/env python3
""" task 5.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """push list of float
    """
    pat = 0
    for item in input_list:
        pat += item

    return pat
