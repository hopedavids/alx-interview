#!/usr/bin/env python3

""" This script that determines if a given data set represents
    a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ This method that determines if a given data set represents
        a valid UTF-8 encoding.
    """
    # Initialize a variable to track the number of bytes in the char
    num_bytes = 0

    # Iterate through each byte in the data
    for byte in data:
        # Check if it's a continuation byte (starts with 10)
        if byte >> 6 == 0b10:
            # If num_bytes is 0, this is an invalid continuation byte
            if num_bytes == 0:
                return False
            # Decrease num_bytes for each continuation byte
            num_bytes -= 1
        # Check if it's the start of a new character (starts with 0 or 11)
        elif byte >> 7 == 0b0:
            # If num_bytes is not 0, there is an ongoing character
            if num_bytes != 0:
                return False
        elif byte >> 5 == 0b110:
            num_bytes = 1
        elif byte >> 4 == 0b1110:
            num_bytes = 2
        elif byte >> 3 == 0b11110:
            num_bytes = 3
        else:
            # Invalid starting byte for a character
            return False

    # If num_bytes is not 0 at the end, there's an incomplete character
    return num_bytes == 0
