#!/usr/bin/python3
"""This module has the print_square() function"""


def print_square(size):
    """ function that render a square rendered with "#" according with size

    Args:
        size:   The size of the desired square must be an integer >= 0

        This function Returns Nothing prints the square in the stdout
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
