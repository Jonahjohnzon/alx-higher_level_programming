#!/usr/bin/python3
"""square-printing function."""


def print_square(size):
    """print square

    Args:
    size: the size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
