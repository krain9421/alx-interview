#!/usr/bin/python3

"""
Module for solving Prime Game Problem
"""


def isWinner(x, nums):
    """
    Function that determines the
    winner of the Prime Game
    """

    def SieveOfEratosthenes(n):
        """
        # Create a boolean array
        # "prime[0..n]" and initialize
        #  all entries it as true.
        # A value in prime[i] will
        # finally be false if i is
        # Not a prime, else true.
        """
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):

            # If prime[p] is not
            # changed, then it is a prime
            if (prime[p] is True):

                # Update all multiples of p
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1

        # Print all prime numbers
        numPrime = 0
        for p in range(2, n+1):
            if prime[p]:
                numPrime += 1

        return numPrime

    # Beginning of the main Prime Game Function
    if (x > 10000):
        return (None)

    for n in nums:
        if (n > 10000):
            return (None)

    mariaWins = 0
    benWins = 0

    for num in nums:
        numPrime = SieveOfEratosthenes(num)
        if (numPrime % 2 == 0):
            benWins += 1
        else:
            mariaWins += 1

    if (benWins > mariaWins):
        return ("Ben")
    elif (mariaWins > benWins):
        return ("Maria")
    else:
        return (None)
