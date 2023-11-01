#!/usr/bin/python3
"""
All about Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal's triangle of n
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            here = 1
            for j in range(1, i + 1):
                level.append(here)
                here = here * (i - j) // j
            res.append(level)
    return res
