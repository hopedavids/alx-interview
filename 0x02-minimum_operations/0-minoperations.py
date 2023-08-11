#!/usr/bin/python3

""" Minimum Operations: In a text file, there is a single character H """


def minOperations(n):
    """ In a text file, there is a single character H. Your text editor can
        execute only two operations in this file: Copy All and Paste. Given
        a number n, write a method that calculates the fewest number of
        operations needed to result in exactly n H characters in the file.
    """

    if n <= 1:
        return 0

    operations = 0
    current_char = 1  # The initial single character 'H'
    clipboard = 0

    while current_char < n:
        if n % current_char == 0:
            clipboard = current_char
            operations += 1  # Copy All
        current_char += clipboard  # Paste
        operations += 1

    return operations
