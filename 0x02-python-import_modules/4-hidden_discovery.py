#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for function in dir(hidden_4):
        if function[1] != "_":
            print(function)
