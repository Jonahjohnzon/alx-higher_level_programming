#!/usr/bin/python3
"""Find a peak in list of unsorted integers"""


def find_peak(list_of_integers):
    """Function"""

    if list_of_integers is None or list_of_integers == []:
        return None

    start, end = 0, len(list_of_integers)
    middle = (start + end) // 2

    if end == 2:
        return max(list_of_integers)

    if list_of_integers[middle] >= list_of_integers[middle - 1] and \
            list_of_integers[middle] >= list_of_integers[middle + 1]:
        return list_of_integers[middle]

    if middle > 0 and list_of_integers[middle] < list_of_integers[middle + 1]:
        return find_peak(list_of_integers[middle:])
    elif middle > 0 and list_of_integers[middle] < list_of_integers[middle - 1]:
        return find_peak(list_of_integers[:middle])
