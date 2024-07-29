#!/usr/bin/python3
"""
Module for validating UTF-8 data
"""


def validUTF8(data):
    """
    Checks if a given data set represents
    a valid UTF-8 encoding

    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data,
        therefore you only need to handle the
        8 least significant bits of each integer
    """
    i = 0  # Index of the list
    over_bytes = 0  # Stores number of extra bytes
    pass_byte = 0  # Stores number of bytes to skip
    for byte in data:
        if pass_byte > 0:
            pass_byte -= 1
            i = i + 1
            pass
        elif not over_bytes:
            if (byte & 0x80) == 0:
                # LOGGING
                # print("1 BYTE UTF-8")
                pass
            elif (byte & 0xe0) == 0xc0:
                over_bytes = 1
                # LOGGING
                # print("2 BYTE UTF-8")
            elif (byte & 0xf0) == 0xe0:
                over_bytes = 2
                # LOGGING
                # print("3 BYTE UTF-8")
            elif (byte & 0xf8) == 0xf0:
                over_bytes = 3
                # LOGGING
                # print("4 BYTE UTF-8")
            else:
                # LOGGING
                # print("INVALID UTF-8")
                return False
        else:
            end = i + over_bytes
            if end > len(data):
                return False
            for byt in data[i:end]:
                # LOGGING
                # print(data[i:end])
                if (byt & 0xc0) != 0x80:
                    # LOGGING
                    # print("INVALID UTF-8")
                    return False
            pass_byte = over_bytes
            over_bytes = 0
        i = i + 1  # Increment the index after every iteration

        # Check if dataset is shorter than over_bytes
        if (over_bytes and i + over_bytes > len(data)):
            return False
    return True
