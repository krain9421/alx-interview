#!/usr/bin/python3
"""
Module for solving the N Queens problem
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    arg = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

"""
if not isinstance(arg, int):
    print("N must be a number")
    sys.exit(1)
"""

if arg < 4:
    print("N must be at least 4")
    sys.exit(1)


# If all checks pass, proceed with N Queen logic
def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check this column on upper side
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    result = []
    board = [-1] * n
    solve(board, 0)

    # Convert the board representation to coordinates
    solutions = []
    for sol in result:
        coordinates = [[i, sol[i]] for i in range(n)]
        solutions.append(coordinates)

    return solutions


solutions = solve_n_queens(arg)
for solution in solutions:
    print(solution)
