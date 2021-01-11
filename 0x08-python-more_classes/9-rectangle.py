#!/usr/bin/python3
"""This module has an Empty class 'Rectangle'."""


class Rectangle:
    """ Model of a rectangle. """

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """ Creates a new instance with same width and height dimensions. """

        return cls(size, size)

    def bigger_or_equal(rect_1, rect_2):
        """ Evaluates which rectangle has the biggest area

            Args:
                rect_1:     A valid rectangle instance.
                rect_2:     A valid rectangle instance.

            Returns:
                The one with the biggest area (or rect_1 if areas are equal)
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __init__(self, width=0, height=0):
        """ Constructor for Rectangle instance

            Args:
                width (optional):   The rectangle width (0 by default)
                height (optional):  The rectangle height (0 by default)
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """ setter for width property """

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
                printable += (str(self.print_symbol) * self.width) + "\n"
            printable += (str(self.print_symbol) * self.width)
        return printable

    def __repr__(self):
        """ repr representation of a Rectangle object """

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ destructor for Rectangle object. Prints a message """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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
    doctest.testfile("tests/8-rectangle.txt")
