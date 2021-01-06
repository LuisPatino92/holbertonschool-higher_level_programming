#!/usr/bin/python3
""" This module has the definition of  a Square class"""


class Square:
    """Model of a square """
    def __init__(self, size=0, position=(0, 0)):
        """ Constructor for Square Method

            Args:
                size (int): Is the size of the instance, 0 by default.
                position (tuple): Is a tuple of two ints, represents
                    the position of the square instance.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or \
                len(position) != 2 or \
                not isinstance(position[0], int) or \
                not isinstance(position[1], int) or \
                position[0] < 0 or \
                position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ Getter of position property

        Returns: The position of the instance
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter of position property

        Args:
            value (tuple of (int, int)): The position to be set in the Square
                instance
        """
        if not isinstance(position, tuple) or \
                len(position) != 2 or \
                not isinstance(position[0], int) or \
                not isinstance(position[1], int) or \
                position[0] < 0 or \
                position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """ Prints a square filling # pattern according to size"""

        if self.__size > 0:
            for _ in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print("{}{}".format(" " * (self.__position[0]),
                                    "#" * self.__size))
        else:
            print("")


    def __str__(self):
        """ Generate the pattern to be printed through print()

        Returns: The str representation of the object
        """
        output = ""
        for _ in range(self.__position[1]):
            output += "\n"

        if self.__size > 0:
            for i in range(self.__size):
                output += "{}{}\n".format(" " * (self.__position[0]),
                                          "#" * self.__size)
        else:
            output += "\n"
        return output[0:-1]
