#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for key in a_dictionary:
            if a_dictionary[key] == value:
                a_dictionary.pop(key)
                break
    return a_dictionary
