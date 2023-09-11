#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n_l = []
    length = len(my_list)
    for i in range(length):
        if (my_list[i] % 2 == 0):
            n_l.append(True)
        else:
            n_l.append(False)
    return n_l
