#!/usr/bin/python3
"""This module has a function that return the names attached to an object"""


def lookup(obj):
    """Function that returns the list of names of an object"""
    return dir(obj)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-test.txt")
