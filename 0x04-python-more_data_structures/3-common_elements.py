#!/usr/bin/python3
def common_elements(set_1, set_2):
    added = []
    common = []
    for element in set_1:
        if element in set_2:
            if element not in added:
                added += [element]
                common += [element]
    return set(common)
