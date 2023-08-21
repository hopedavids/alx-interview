#!/usr/bin/env python3

""" This script that reads stdin line by line and computes metrics: """

import sys
import signal

total_size = 0
status_count = {}


def print_metrics(signum, frame):
    """ Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
        <status code> <file size> (if the format is not this one, the line
        must be skipped). After every 10 lines and/or a keyboard interruption
        (CTRL + C), print these statistics from the beginning:
    """

    print(f"File size: {total_size}")
    for status_code in sorted(status_count.keys()):
        print(f"{status_code}: {status_count[status_code]}")
    sys.exit(0)


# Set up the signal handler for keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, print_metrics)

# Read input lines from stdin
for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) >= 7:
        ip_address, _, _, _, _, status_code, file_size = parts
        try:
            file_size = int(file_size)
            total_size += file_size
            status_code = int(status_code)
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_count[status_code] = status_count.get(status_code, 0) + 1
        except ValueError:
            continue

        # Check if it's time to print metrics
        if len(status_count) == 8 or total_size >= 10:
            print_metrics(None, None)
