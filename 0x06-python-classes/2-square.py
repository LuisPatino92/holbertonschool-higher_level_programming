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
