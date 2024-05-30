#!/usr/bin/python3
"""Module that defines a function that prints Pascal's triangle"""


def pascal_triangle(n):
    """
    function that generates Pascal's triangle up to nth row

    Args:
      n (int): Number of rows to generate

    Return:
      List[List[int]]: A list of lists representing Pascal's triangle
    """

    if n <= 0:
        return []  # Return empty list for non-positive n

    triangle = []  # Declare list to store triangle

    for i in range(n):  # For each row of the triangle
        row = []  # Declare an empty list for each row

        for j in range(i + 1):  # For each column in a row
            row.append(0)  # Fill the row with 0 values

        for k in range(i + 1):  # For each column in a row
            if (i + 1 == 1):  # If currently on first row
                row[k] = 1
            else:  # If not on the first row
                if (k == 0 or k == i):  # If either on the first or last column
                    row[k] = 1
                else:
                    row[k] = row_tmp[k-1] + row_tmp[k]

        row_tmp = row
        triangle.append(row)

    return triangle
