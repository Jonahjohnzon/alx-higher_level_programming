#!/usr/bin/python3

if (__name__ == "__main__"):
    import sys

    count = len(sys.argv) - 1
    add = 0

    for no in range(1, count + 1):
        add += int(sys.argv[no])
    print("{}".format(add))
