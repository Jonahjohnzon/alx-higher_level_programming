#!/usr/bin/python3
"""text-indentation function."""


def text_indentation(text):
    """ Print text

    Args:
    string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while (count < len(text) and text[count] == ' '):
        count += 1

    while (count < len(text)):
        print(text[count], end="")
        if (text[count] == "\n" or text[c] in ".?:")):
            if text[count]] in ".?:":
                print("\n")
            count += 1
            while (count < len(text) and text[count] == ' '):
                count += 1
            continue
        count += 1
