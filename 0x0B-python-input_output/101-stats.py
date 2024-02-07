#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""


def print_stats(size, status_codes):
    """print the sumed metrics"""
    print("File size: {}".format(size))
    for i in sorted(status_codes):
        print("{}: {}".format(i, status_codes[i]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for j in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            j = j.split()

            try:
                size += int(j[-1])
            except (IndexError, ValueError):
                pass

            try:
                if j[-2] in valid_codes:
                    if status_codes.get(j[-2], -1) == -1:
                        status_codes[j[-2]] = 1
                    else:
                        status_codes[j[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
