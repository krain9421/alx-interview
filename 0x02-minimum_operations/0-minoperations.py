#!/usr/bin/python3
"""
Module to compute minimum operations
"""
from typing import Tuple


def get_factors(n):
    """
    Function gets the min and max factors
    of a number `n`
    """
    if n == 1:
        return 1, 1
    if n == 0:
        return 0, 0
    for i in range(2, (int(n / 2) + 1)):
        if n / i == n // i:
            return i, int(n / i)
    return 1, n


def minOperations(n):
    """
    Function calculates the minimum number
    of operations to get `n` number of characters
    """
    if n <= 1:
        return 0
    # Get the min and max factors of n
    min_f, max_f = get_factors(n)
    if min_f == 1:
        return max_f
    if min_f == 0:
        return 0
    return min_f + minOperations(max_f)
