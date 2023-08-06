#!/usr/bin/python3

from typing import List

"""
You have n number of locked boxes in front of you. Each box is
numbered sequentially from 0 to n - 1 and each box may contain keys
to the other boxes. Write a method that determines if all the boxes
can be opened. Prototype: def canUnlockAll(boxes) boxes is a list of
lists. A key with the same number as a box opens that box You can
assume all keys will be positive integers.There can be keys that do
not have boxes. The first box boxes[0] is unlocked. Return True if
all boxes can be opened, else return False.
"""


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """ This method that determines if all the boxes can be opened. """

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
