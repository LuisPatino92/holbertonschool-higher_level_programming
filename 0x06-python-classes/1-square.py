#!/usr/bin/python3
""" This module has the definition of  a Square class"""


class Square:
    """ Model of a square """

    def __init__(self, size):
        """ Constructor for Square Method

            Args:
                size (int): Is the size of the instance, 0 by default.
        """
        self.__size = size
