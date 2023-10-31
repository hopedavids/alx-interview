#!/usr/bin/python3
"""
log parsing
"""

import sys


def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))


total_size = 0
status_counts = {}

try:
    for line_number, line in enumerate(sys.stdin, start=1):
        line = line.strip()
        parts = line.split()
        if len(parts) >= 7:
            status_code = parts[-2]
            file_size = int(parts[-1])

            total_size += file_size

            if status_code.isdigit():
                status_code = int(status_code)
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if line_number % 10 == 0:
                print_stats(total_size, status_counts)

except KeyboardInterrupt:
    pass

print_stats(total_size, status_counts)
