#!/usr/bin/python3
def multiple_returns(sentence):
    new_s = ()
    if (len(sentence) == 0):
        new_s = 0, "None"
    else:
        new_s = len(sentence), sentence[0]
    return new_s
