#!/usr/bin/python3
"""This module has The class BaseGeometry"""


class BaseGeometry():
    """Empty class for rectangle and square modeling"""

    def area(self):
        """Not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if an object is an integer greater than 0"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
