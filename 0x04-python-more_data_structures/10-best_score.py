#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary):
        keys = list(a_dictionary.keys())
        highest = 0
        top = ""
        for key in keys:
            if (a_dictionary[key] > highest):
                highest = a_dictionary[key]
                top = key
        return top
