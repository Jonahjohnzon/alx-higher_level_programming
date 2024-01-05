#!/usr/bin/python3
"""Find a peak in list of unsorted integers"""


def find_peak(list_of_integers):
    """Funtion"""

    if list_of_integers is None or list_of_integers == []:
        return None
    l = 0
    hi = len(list_of_integers)
    middle = ((hi - l) // 2) + l
    middle = int(middle)
    if hi == 1:
        return list_of_integers[0]
    if hi == 2:
        return max(list_of_integers)
    if list_of_integers[middle] >= list_of_integers[middle - 1] and\
            list_of_integers[middle] >= list_of_integers[middle + 1]:
        return list_of_integers[middle]
    if middle > 0 and list_of_integers[middle] < list_of_integers[middle + 1]:
        return find_peak(list_of_integers[middle:])
    if middle > 0 and list_of_integers[middle] < list_of_integers[middle - 1]:
        return find_peak(list_of_integers[:middle])
