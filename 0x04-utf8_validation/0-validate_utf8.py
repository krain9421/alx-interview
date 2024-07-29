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
    pass_byte = 0
    for byte in data:
        if pass_byte > 0:
            pass_byte -= 1
            pass
        elif not over_bytes:
            if (byte & 0x80) == 0:
                pass
            elif (byte & 0xe0) == 0xc0:
                over_bytes = 1
            elif (byte & 0xf0) == 0xe0:
                over_bytes = 2
            elif (byte & 0xf8) == 0xf0:
                over_bytes = 3
            else:
                return False
        else:
            end = i + over_bytes
            if end >= len(data):
                return False
            for byt in data[i:end]:
                if (byt & 0xc0) != 0x80:
                    return False
            pass_byte = over_bytes
            over_bytes = 0
    return True
