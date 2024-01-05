#!/usr/bin/python3
"""Find a peak in list of unsorted integers"""


def find_peak(list_of_integers):
    """Function"""

    if list_of_integers is None or list_of_integers == []:
        return None

    lo, hi = 0, len(list_of_integers)
    midd = (lo + hi) // 2

    if hi == 2:
        return max(list_of_integers)

    if list_of_integers[midd] >= list_of_integers[midd - 1] and \
            list_of_integers[midd] >= list_of_integers[midd + 1]:
        return list_of_integers[midd]

    if midd > 0 and list_of_integers[midd] < list_of_integers[midd + 1]:
        return find_peak(list_of_integers[midd:])
    elif midd > 0 and list_of_integers[midd] < list_of_integers[midd - 1]:
        return find_peak(list_of_integers[:midd])
