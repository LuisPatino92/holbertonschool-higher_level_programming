#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    print("{} ".format(len(argv) - 1), end="")
    if len(argv) == 2:
        print("argument", end="")
    else:
        print("arguments", end="")

    if len(argv) == 1:
        print(".")
    else:
        print(":")

    if len(argv) > 1:
        i = 1
        for arg in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
            i += 1
