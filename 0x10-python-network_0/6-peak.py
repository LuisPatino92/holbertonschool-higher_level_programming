#!/usr/bin/python3
"""This module has the find_peak function"""


def find_peak(list_of_integers):
    """Returns the peak of a list """

    if len(list_of_integers) == 0:
        a = None
    else:
        a =list_of_integers.sort()[-1]

    return a
