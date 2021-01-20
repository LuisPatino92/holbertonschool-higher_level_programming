#!/usr/bin/python3
"""This module has the function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Checks if a object is from a class or an inherited one

    Args:
        obj:        any object
        a_class:    The class you want to check if obj is an instance of

    Return:         True if obj is an instance of a_class or derived,
                    False otherwise.
    """
    return issubclass(type(obj), a_class)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-test.txt")
