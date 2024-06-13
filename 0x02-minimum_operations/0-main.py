#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations
##isPrime = __import__('0-minoperations').isPrime

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 19170307
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

##n = 2147483640
##print("It is {} that {} is a prime number".format(isPrime(n), n))
