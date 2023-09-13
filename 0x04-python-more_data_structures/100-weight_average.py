#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    number = 0
    denom = 0

    for lis in my_list:
        number += lis[0] * lis[1]
        denom += lis[1]
    return (number / denom)
