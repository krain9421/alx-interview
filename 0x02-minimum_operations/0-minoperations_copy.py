#!/usr/bin/python3
"""Module for performing minimum operations"""


def minOperations(n):
    """
    function that calculates the fewest operations
    needed to result in exactly `n` characters

    returns an integer
    If n is impossible to achieve, return 0
    """

    if n <= 1:
        return 0

    operations = 0
    current = 1

    while current < n:
        if n % current == 0:
            operations += n / current
            current *= n / current
        else:
            return 0

    return operations
