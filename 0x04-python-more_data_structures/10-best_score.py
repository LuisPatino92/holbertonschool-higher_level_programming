#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    mayor = int(0)
    bestScore = str("")
    for element in a_dictionary.keys():
        if int(a_dictionary[element]) > mayor:
            mayor = int(a_dictionary[element])
            best_score = element
    return best_score
