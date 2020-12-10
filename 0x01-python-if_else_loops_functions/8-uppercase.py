#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if 97 <= ord(letter) <= 122:
            msg = chr(ord(letter) - 32)
        else:
            msg = letter
        print("{}".format(msg), end="")
    print("")
