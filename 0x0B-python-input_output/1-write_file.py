#!/usr/bin/python3
"""function that reads file"""


def write_file(filename="", text=""):
    """Write in file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
