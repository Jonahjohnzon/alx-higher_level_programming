#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if (length == 0):
        return "None"
    else:
        maxx = my_list[0]
        for c in range(length):
            if my_list[c] > maxx:
                maxx = my_list[c]
        return maxx
