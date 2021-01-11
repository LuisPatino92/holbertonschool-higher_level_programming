#!/usr/bin/python3
""" This module has the class 'Rectangle'. """


class Rectangle:
    """ Model of a rectangle. """

    def __init__(self, width=0, height=0):
        """ Constructor for Rectangle instance

            Args:
                width (optional):   The rectangle width (0 by default)
                height (optional):  The rectangle height (0 by default)
        """

        self.width = width
        self.height = height

    @property
    def height(self):
        """ getter for height property """

        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height property """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ getter for width property """

        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width property """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def __str__(self):
        """ str representation of a Rectangle object """

        printable = ""
        if not (self.height == 0 or self.width == 0):
            for i in range(self.height - 1):
                printable += ("#" * self.width) + "\n"
            printable += ("#" * self.width)
        return printable

    def __repr__(self):
        """ repr representation of a Rectangle object """

        return "Rectangle({}, {})".format(self.width, self.height)

    def area(self):
        """ Computes and returns the area of a Rectangle object """

        return self.height * self.width

    def perimeter(self):
        """ Computes and returns the perimeter of a Rectangle object """

        if self.height == 0 or self.width == 0:
            return 0
        return 2 * self.height + 2 * self.width


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-rectangle.txt")
