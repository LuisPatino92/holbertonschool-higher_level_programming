#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    added = []
    new_set = []
    for element in set_1:
        if element not in set_2 and element not in added:
            new_set += [element]
        added += [element]
    for element in set_2:
        if element not in set_1 and element not in added:
            new_set += [element]
        added += [element]
    return set(new_set)
