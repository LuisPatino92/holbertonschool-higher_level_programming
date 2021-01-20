#!/usr/bin/python3
"""This module has the function is_same_class"""


def is_same_class(obj, a_class):
    """Returns True if obj is an instance of a_class, False otherwise

    Args:
        obj:        any object
        a_class:    The class you want to check if obj is an instance of

    Return:         True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) == a_class

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
