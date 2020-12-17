#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mayor = int()
    bestScore = str()
    for element in a_dictionary.keys():
        if int(a_dictionary[element]) > mayor:
            mayor = int(a_dictionary[element])
            best_score = element
    if mayor is None:
        return None
    return element
