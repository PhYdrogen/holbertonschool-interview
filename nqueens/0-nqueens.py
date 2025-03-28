#!/usr/bin/python3
"""
N Queens puzzle solver
The N queens puzzle is the challenge of placing N non-attacking queens on
an NxN chessboard
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]

    Args:
        board: 1D array where board[i] represents the column where a queen
              is placed in row i
        row: current row to check
        col: current column to check
        n: size of the board

    Returns:
        Boolean: True if safe, False otherwise
    """
    # Check for queens in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i] == j:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N queens problem and print all solutions

    Args:
        n: size of the board and number of queens
    """
    board = [-1] * n
    solutions = []

    def backtrack(row):
        if row == n:
            # Found a solution, add it to our list
            solution = [[i, board[i]] for i in range(n)]
            solutions.append(solution)
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                # Backtrack
                board[row] = -1

    backtrack(0)
    return solutions


def main():
    """Main function to handle input and solve the N Queens problem"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
