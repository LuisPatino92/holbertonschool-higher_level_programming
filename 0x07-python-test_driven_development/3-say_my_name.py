#!/usr/bin/python3
"""This module has the say_my_name_function"""


def say_my_name(first_name, last_name=""):
    """ Functions that say your name

    Args:
        first_name:     The first name (mandatory)
        last_name:      The last name (optional)

    This function doesn't return nothing, prints in stdout the message:
        My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
