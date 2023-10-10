#!/usr/bin/python3
"""
FUNTION
"""


def p_stats(siz, status_codes):
    """Print accumulated METRIC
    """
    print("File size: {}".format(siz))
    for x in sorted(status_codes):
        print("{}: {}".format(x, status_codes[x]))


if __name__ == "__main__":

    import sys

    siz = 0
    status_codes = {}
    _codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for li in sys.stdin:
            if (count == 10):
                p_stats(siz, status_codes)
                count = 1
            else:
                count += 1

            li = li.split()

            try:
                siz += int(li[-1])
            except (IndexError, ValueError):
                pass

            try:
                if li[-2] in _codes:
                    if (status_codes.get(li[-2], -1) == -1):
                        status_codes[li[-2]] = 1
                    else:
                        status_codes[li[-2]] += 1
            except IndexError:
                pass
        p_stats(siz, status_codes)

    except KeyboardInterrupt:
        p_stats(siz, status_codes)
        raise
