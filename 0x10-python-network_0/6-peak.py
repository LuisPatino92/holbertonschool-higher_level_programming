#!/usr/bin/python3
"""This module has the find_peak function"""


def find_peak(list_of_integers):
    """Returns the peak of a list """

    return list_of_integers.sort()[-1]
