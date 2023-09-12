#!/usr/bin/python3

""" Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""

from typing import List


def rotate_2d_matrix(matrix: List[List]):
    """ Prototype: def rotate_2d_matrix(matrix):
        Do not return anything. The matrix must be edited in-place.
        You can assume the matrix will have 2 dimensions and will not be empty.
    """

    # Replica Matrix
    replica = matrix[:]

    for i in range(len(matrix)):
        # retract column from replica
        column = [row[i] for row in replica]
        # Replace in matrix in reverse order
        matrix[i] = column[::-1]
