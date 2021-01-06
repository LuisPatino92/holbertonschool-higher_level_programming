#!/usr/bin/python3
""" This module has the definition of  a Square class"""


class Square:
    """ Model of a square """

    def __init__(self, size=0):
        """ Constructor for Square Method

            Args:
                size (int): Is the size of the instance, 0 by default.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Returns the area of the square

        Returns: The area of the Square instance
        """
        return self.__size ** 2

    @property
    def size(self):
        """ Getter of size property

        Returns: The size of the Square instance
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter of size property

        Args:
            value (int): The size to be set in the Square instance
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
