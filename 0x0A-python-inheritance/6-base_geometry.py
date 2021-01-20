#!/usr/bin/python3
"""This module has The class BaseGeometry"""


class BaseGeometry():
    """Empty class for rectangle and square modeling"""

    def area(self):
        """Not implemented yet"""
        raise Exception("area() is not implemented")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/6-test.txt")
