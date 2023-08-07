#!/usr/bin/python3

from typing import List

"""
    Lockboxes Contains method that finds the keys to
    open other lockboxes
"""


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Function that determines if you can open all the lockboxes
    Args:
        boxes: list of lists of integers
    Returns:
        True if you can open all the lockboxes, False otherwise
    """

    n = len(boxes)
    visited = [False] * n
    stack = [0]  # Start with the first box (boxes[0])
    visited[0] = True

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and not visited[key]:
                stack.append(key)
                visited[key] = True

    return all(visited)
