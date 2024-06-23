#!/usr/bin/python3
"""Module for reading from stdin and printing computes metrics
"""


def printer(filesize, status_codes):
    """
    Function that prints computer metrics
    """
    stats = ""
    # Write the format into stats
    stats += "File size: {}\n".format(filesize)
    for n in sorted(status_codes):
        if status_codes[n] > 0:
            stats += "{}: {}\n".format(n, status_codes[n])
    print(stats[:-1])


if __name__ == '__main__':
    """Main function signifying entry to the program
    """

    import sys
    filesize = 0
    status_codes = {
            200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
            }
    i = 1
    try:
        for line in sys.stdin:
            # Parse the line
            data_list = line.split(" ")
            # Get the status code from line
            status_in = data_list[-2]
            # Get the file size from line
            filesize_in = data_list[-1]

            # Increment the corresponding status code if...
            if int(status_in) in status_codes:
                status_codes[int(status_in)] += 1

            # Increment the file size
            filesize += int(filesize_in)

            # Condition for every 10 lines of stdin
            if i % 10 == 0:
                printer(filesize, status_codes)
                i += 1
            else:
                i += 1

        printer(filesize, status_codes)
    except KeyboardInterrupt as e:
        printer(filesize, status_codes)
