#!/usr/bin/python3
"""Rectangle class, inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """Model of a Rectangle, Inherits id mechanism from Base
       Args:
            width (int):    The width of the Rectangle object
            height (int):   The height of the Rectangle object
            x (int) (opt):  X position of the Rectangle object (0 by default)
            y (int) (opt):  Y position of the rectangle object (0 by default)
            id (int) (opt): The id of the objrct (class.__nb_objects by def)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        "Constructor for a Rectangle, parameters as defined in class doc"

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for Rectangle's width Property"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for Rectangle's width Property"""

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter for Rectangle's height Property"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for Rectangle's height Property"""

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter for Rectangle's x Property"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for Rectangle's x Property"""

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getter for Rectangle's y Property"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for Rectangle's y Property"""

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of the Rectangle object"""

        return self.height * self.width

    def display(self):
        """Renders the rectangle using '#' symbol as base"""

        print("\n" * self.y, end="")

        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """str representation of a rectangle"""

        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id,
                                                self.x,
                                                self.y,
                                                self.width,
                                                self.height)

    def update(self, *args, **kwargs):
        """Updates the attributes using *args

        Args expected order: id, width, height, x, y
        """
        if len(args) > 0:
            atts = ['id', 'width', 'height', 'x', 'y']

            for attribute, new_val in zip(atts, args):
                setattr(self, attribute, new_val)
        else:
            for element in kwargs:
                setattr(self, element, kwargs[element])

    def to_dictionary(self):
        """Returns the dictionary representation of the object's state"""
        obj_dict = self.__dict__.copy()
        for ele in obj_dict.keys():
            if "_Rectangle__" in ele:
                obj_dict[ele.replace("_Rectangle__", "")] = self.__dict__[ele]
                obj_dict.pop(ele)
        return obj_dict
