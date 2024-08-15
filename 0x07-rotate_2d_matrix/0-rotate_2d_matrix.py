#!/usr/bin/python3
"""
Module for implementing rotation of a 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    Matrix must be edited in-place.
    Matrix will have 2 dimensions and will not be empty.
    """
    # Create a copy of the matrix to be used in the loop
    matrix_tmp = matrix.copy()

    for i in range(len(matrix_tmp)):
        transposed_row = []
        for row in matrix_tmp:
            transposed_row.append(row[i])
        transposed_row.reverse()
        matrix[i] = transposed_row

    # Clear the matrix copy
    matrix_tmp.clear()
