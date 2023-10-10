#!/usr/bin/python3
"""text file function"""


def append_after(filename="", search_string="", new_string=""):
    """function"""

    txt = ""

    with open(filename) as f:
        for line in f:
            txt += line
            if (search_string in line):
                txt += new_string
    with open(filename, "w") as writ:
        writ.write(txt)
