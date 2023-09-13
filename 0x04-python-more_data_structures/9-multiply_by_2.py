#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_list = {}
    for k, v in a_dictionary.items():
        new_list.update({k: (v * 2)})
    return new_list
