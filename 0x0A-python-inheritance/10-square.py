#!/usr/bin/python3
"""Module with a Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Model of a square"""

    def __init__(self, size):
        """Constructor for square Object"""
        super().__init__(size, size)
        self.size = size

    def area(self):
        """Sets the area of the square"""

        return self.size ** 2
