#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set(my_list)
    new_list = list(new_set)
    number = 0
    for i in new_list:
        number += i
    return number
