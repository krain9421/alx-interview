#!/usr/bin/python3
"""This module reads stdin and computes metrics
"""


import sys
import signal
import os

line = []
st_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
           "403": 0, "404": 0, "405": 0, "500": 0}
global file_size
file_size = 0
interrupted = False


def signal_handler(signum, frame):
    """Signal handler function to handle
        keyboard interrupt
    """

    global interrupted
    interrupted = True
    print_stats(file_size = 0)


def checker(line):
    """Function that checks if a line is of a specific format
    """

    st_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    checknum = 0
    if (len(line[0].split(".")) == 4):
        checknum = checknum + 1
    if (line[1] == "-"):
        checknum = checknum + 1
    if (line[2]):
        checknum = checknum + 1
    if (line[3]):
        checknum = checknum + 1
    if (line[4] == "\"GET"):
        checknum = checknum + 1
    if (line[5] == "/projects/260"):
        checknum = checknum + 1
    if (line[6] == "HTTP/1.1\""):
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


def print_stats(file_size):
    """Function that prints out statistics
    """

    for i in range(10):
        line = sys.stdin.readline().split()  # Get a line from stdin
        if (checker(line)):
            file_size = file_size + int(line[8])
            st_dict[line[7]] = st_dict[line[7]] + 1
            # print(line)
        else:
            pass
    print("File size: {}".format(file_size))
    for k in st_dict:
        print("{}: {}".format(k, st_dict[k]))

    file_size = 0  # Resetting file_size to 0
    for k in st_dict:  # Resetting the values in st_dict to 0
        st_dict[k] = 0


# Set the signal hanler for SIGINT (KeyboardInterrupt)
# signal.signal(signal.SIGINT, signal_handler)

try:
    while True:
        print_stats(file_size)
        # if interrupted:
        #    break
except KeyboardInterrupt:
    print_stats(file_size=0)
