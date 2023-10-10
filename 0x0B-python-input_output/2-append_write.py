#!/usr/bin/python3
"""append file"""


def append_write(filename="", text=""):
    """append a string to file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
