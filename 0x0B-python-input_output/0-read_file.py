#!/bin/python3
"""function that reads file"""


def read_file(filename=""):
    """Print"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
