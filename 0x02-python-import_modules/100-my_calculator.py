#!/usr/bin/python3
import calculator_1 as c
from sys import exit
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    elif not argv[2] in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif argv[2] == "+":
        print(c.add(int(argv[1]), int(argv[3])))
    elif argv[2] == "-":
        print(c.sub(int(argv[1]), int(argv[3])))
    elif argv[2] == "*":
        print(c.mul(int(argv[1]), int(argv[3])))
    elif argv[2] == "/":
        print(c.div(int(argv[1]), int(argv[3])))
