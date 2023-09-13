#!/usr/bin/python3
def common_elements(set_1, set_2):
    lists = []
    for i in set_1:
        for o in set_2:
            if (i == o):
                lists.append(i)
    return lists
