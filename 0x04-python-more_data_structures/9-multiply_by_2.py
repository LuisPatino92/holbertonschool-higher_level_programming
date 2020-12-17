#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for element in a_dictionary.keys():
        new_dictionary.update({element: a_dictionary[element] * 2})
    return new_dictionary
