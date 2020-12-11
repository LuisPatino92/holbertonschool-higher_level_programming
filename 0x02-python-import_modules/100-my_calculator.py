#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import exit
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif not argv[2] in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif argv[2] == "+":
        print(add(int(argv[1]), int(argv[3])))
    elif argv[2] == "-":
        print(sub(int(argv[1]), int(argv[3])))
    elif argv[2] == "*":
        print(mul(int(argv[1]), int(argv[3])))
    elif argv[2] == "/":
        print(div(int(argv[1]), int(argv[3])))
