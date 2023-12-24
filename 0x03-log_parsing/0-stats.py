#!/usr/bin/python3
"""Module containing a script that reads stdin and computes metrics"""
import random
import sys
from time import sleep
import datetime


line = []
st_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
           "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0
while (True):
    for i in range(10):
        line = sys.stdin.readline().split()
        file_size = file_size + int(line[8])
        st_dict[line[7]] = st_dict[line[7]] + 1
        # print(line)
    print("File size: {}".format(file_size))
    for k in st_dict:
        print("{}: {}".format(k, st_dict[k]))

    file_size = 0  # Resetting file_size to 0
    for k in st_dict:  # Resetting the values in st_dict to 0
        st_dict[k] = 0
