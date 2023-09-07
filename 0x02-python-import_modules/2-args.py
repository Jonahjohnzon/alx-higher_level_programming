#!/usr/bin/python3

if (__name__ == "__main__"):
    import sys

    number = len(sys.argv) - 1
    if (number == 0):
        print("0 arguments.")
    elif (number == 1):
        print("1 argument:")
    else:
        print("{} arguments:".format(number))
    for no in range(1, number + 1):
        print("{}: {}".format(no, sys.argv[no]))
