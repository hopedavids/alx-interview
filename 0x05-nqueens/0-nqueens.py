#!/usr/bin/python3

""" The N queens puzzle is the challenge of placing N non-attacking queens on an NxN
    chessboard. Write a program that solves the N queens problem.
"""

import sys

def is_safe(board, row, col):
    """
    Checks if it is safe to place a queen at (row, col) on the board.

    Args:
        board: The board.
        row: The row index.
        col: The column index.

    Returns:
        True if it is safe to place a queen at (row, col), False otherwise.
    """

    for i in range(row):

        if board[i][col] == 1:
            return False

    for i in range(row):
        if board[i][col - row + i] == 1:
            return False

    for i in range(row):
        if board[i][col + row - i] == 1:
            return False
    return True


def solve_nqueens(board, n):
  """
  Solves the N queens problem for a board of size n.

  Args:
    board: The board.
    n: The size of the board.

  Returns:
    True if the problem was solved, False otherwise.
  """

  if n == 0:
    return True

  for col in range(n):
    if is_safe(board, n - 1, col):
      board[n - 1][col] = 1
      if solve_nqueens(board, n - 1):
        return True
      board[n - 1][col] = 0

  return False


def main():

    """
    The main function.
    """

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

    board = [[0 for i in range(n)] for j in range(n)]

    if solve_nqueens(board, n):
        for i in range(n):
            print(*board[i])
    else:
        print("No solution")    

if __name__ == "__main__":
    main()
