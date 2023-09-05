#!/usr/bin/python3

for n in range(0, 10):
    for n2 in range(n + 1, 10):
        if n == 8 and n2 == 9:
            print("{}{}".format(n, n2))
        else:
            print("{}{}".format(n, n2), end=", ")
