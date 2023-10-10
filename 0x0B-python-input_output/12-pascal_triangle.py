#!/usr/bin/python3
"""pascal_triangle"""


def pascal_triangle(n):
    """Pascal triangle"""

    if (n <= 0):
        return []

    t = [[1]]
    while (len(t) != n):
        tri = t[-1]
        tmps = [1]
        for x in range(len(tri) - 1):
            tmps.append(tri[x] + tri[x + 1])

        tmps.append(1)
        t.append(tmps)

    return t
