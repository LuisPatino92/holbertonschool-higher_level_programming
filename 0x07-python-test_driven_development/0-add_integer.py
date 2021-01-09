#!/usr/bin/python3
"""This module has a function that sums two integers"""


def add_integer(a, b=98):
    """Sums (integer addition) two integers or floats

    Args:
        a, b: Integers or floats. b has a default value of 98

    Returns:
        The integer addition of both numbers. A exception will be raised
        if the arguments are not Int or Float
    """

    # Checking the quality of inputs:
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if a + 1 == a:
        raise OverflowError("a too large")
    if b + 1 == b:
        raise OverflowError("b too large")

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
