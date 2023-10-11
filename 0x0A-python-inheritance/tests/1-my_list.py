#!/usr/bin/python3
"""list"""


class MyList(list):
    """class"""
    def __init__(self):
        """initialize"""
        super().__init__()

    def print_sorted(self):
        """sorted list"""
        print(sorted(self))
