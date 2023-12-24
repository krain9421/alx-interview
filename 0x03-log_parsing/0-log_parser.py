#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime


def checker(line):
    """
        Function that checks if a line is of a specific format
    """
    st_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    checknum = 0
    if (len(line[0].split(".")) == 4):
        # print("CHECK 0: PASSED")
        checknum = checknum + 1
    if (line[1] == "-"):
        # print("CHECK 1: PASSED")
        checknum = checknum + 1
    if (line[2]):
        # print("CHECK 2: PASSED")
        checknum = checknum + 1
    if (line[3]):
        # print("CHECK 3: PASSED")
        checknum = checknum + 1
    if (line[4] == "\"GET"):
        # print("CHECK 4: PASSED")
        checknum = checknum + 1
    if (line[5] == "/projects/260"):
        # print("CHECK 5: PASSED")
        checknum = checknum + 1
    if (line[6] == "HTTP/1.1\""):
        # print("CHECK 6: PASSED")
        checknum = checknum + 1
    if (line[7] in st_codes):
        # print("CHECK 7: PASSED")
        checknum = checknum + 1
    if (int(line[8]) in range(1, 1024)):
        # print("CHECK 8: PASSED")
        checknum = checknum + 1

    if (checknum == 9):
        return True
    else:
        return False


line = []
st_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
           "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0
while (True):
    for i in range(10):
        line = sys.stdin.readline().split()
        if (checker(line)):
            file_size = file_size + int(line[8])
            st_dict[line[7]] = st_dict[line[7]] + 1
            # print(line)
        else:
            pass
    print("File size: {}".format(file_size))
    for k in st_dict:
        print("{}: {}".format(k, st_dict[k]))
