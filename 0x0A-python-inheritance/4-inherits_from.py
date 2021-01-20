#!/usr/bin/python3
"""This module has the function inherits_from"""


def inherits_from(obj, a_class):
    """Checks if a object is from an inherited class

    Args:
        obj:        any object
        a_class:    The class you want to check if obj is an instance of

    Return:         True if obj is an instance of an derived class of a_class,
                    False otherwise.
    """
    return issubclass(type(obj), a_class) and (type(obj) != a_class)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-test.txt")
