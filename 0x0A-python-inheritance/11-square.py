#!/usr/bin/python3
"""Module with a Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Model of a square"""

    def __init__(self, size):
        """Constructor for square Object"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Representation of a Square object"""

        return "[Square] {}/{}".format(self.__size, self.__size)
