#!/usr/bin/python3


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    current_char = 1  # The initial single character 'H'
    clipboard = 0

    while current_char < n:
        if n % current_char == 0:
            clipboard = current_char  # Copy All
        current_char += clipboard  # Paste
        operations += 1

    return operations