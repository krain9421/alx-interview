#!/usr/bin/python3
"""
Module for solving the Coin Change problem with Greedy Algorithm
"""


def makeChange(coins, total):
    """
    Function that calculates the number
    of coins needed to arive at a certain
    total
    """
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)

    num_coins = 0
    for coin in coins:
        if total == 0:
            break
        # Use as many of this coin as possible
        num_coins += total // coin
        total %= coin

    # If total is not zero, it means we cannot meet
    # the total with the given coins
    if total != 0:
        return -1

    return num_coins
