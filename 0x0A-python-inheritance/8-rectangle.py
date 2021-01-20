#!/usr/bin/python3
"""This module has the Rectangle class inherited from base geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherited from BaseGeometry"""

    def __init__(self, width, height):
        """Constructor for Rectangle

        Args:
            width:  The width of the rectangle object
            height: The height of the rectangle object
        """

        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/8-test.txt")
