#!/usr/bin/python3

if (__name__ == "__main__"):
    import sys
    count = len(sys.argv) - 1
    if (count != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        op = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if (op == '+'):
            print("{} {} {} = {}".format(a, op, b, a + b))
        elif (op == '-'):
            print("{} {} {} = {}".format(a, op, b, a - b))
        elif (op == '*'):
            print("{} {} {} = {}".format(a, op, b, a * b))
        elif (op == '/'):
            print("{} {} {} = {}".format(a, op, b, a / b))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
