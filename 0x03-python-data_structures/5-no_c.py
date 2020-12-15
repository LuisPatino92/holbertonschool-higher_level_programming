#!/usr/bin/python3
def no_c(my_string):
    copy = ""
    for letter in my_string:
        if letter != 'C' and letter != 'c':
            copy += letter
    return copy
