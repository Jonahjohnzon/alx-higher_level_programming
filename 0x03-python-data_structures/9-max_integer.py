#!/usr/bin/python3
def max_integer(my_list=[]):
    length(len(my_list))
    if (length == 0):
        return "None"
    else:
        maxs = my_list[0]
        for c in range(len(my_list)):
            if my_list[c] > maxs:
                maxs = my_list[c]
        return maxs
