#!/usr/bin/python3
"""Square Class, inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Model of a Square, Inherits from Rectangle
       Args:
            size (int):     The width of the Square object
            x (int) (opt):  X position of the Rectangle object (0 by default)
            y (int) (opt):  Y position of the rectangle object (0 by default)
            id (int) (opt): The id of the objrct (class.__nb_objects by def)
    """
    def __init__(self, size, x=0, y=0, id=None):
        "Constructor for a Square, parameters as defined in class doc"

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for square's size attribute"""

        return self.width

    @size.setter
    def size(self, value):
        """Setter for square's size attribute"""

        self.width = value
        self.height = value

    def __str__(self):
        """str representation of a square"""

        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.width)

    def update(self, *args, **kwargs):
        """Updates the attributes using *args

        Args expected order: id, width, height, x, y
        """
        if len(args) > 0:
            atts = ['id', 'size', 'x', 'y']

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
        obj_dict["size"] = self.size
        obj_dict.pop("width")
        obj_dict.pop("height")
        return obj_dict
