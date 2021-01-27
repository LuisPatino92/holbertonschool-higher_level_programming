#!/usr/bin/python3
"""Class Base, base for some geometric shapes classes"""

import json


class Base:
    """Base for some geometric shapes. Has an instances counter"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base classes
            Args:
                id (int):   The id of the instance, None by default.
                            if None, the id will take the value of the
                            instances counter (__nb_objects).
        """
        if id is None:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the string representation of a list of dictionaries
           Args:
            list_dictionaries (list of dicts): The list of dictionaries whose
                     representation is desired.
        """
        if list_dictionaries is None:
            return []
        else:
            json_dicts = json.dumps(list_dictionaries)
        return json_dicts

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the JSON rep of a list of objets to a file the name of the
        file will be based on the class name: <classname>.json
        """
        list_dicts = []
        if list_objs is not None:
            for element in list_objs:
                list_dicts += [element.to_dictionary()]
        with open("{}.json".format(cls.__name__), 'w') as f:
            json.dump(list_dicts, f)

    @staticmethod
    def from_json_string(json_string):
        """Constructs a list object with base on the Json representation"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of the calling class
        with the attributes passed in dictionary
        """
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        for element in dictionary:
            setattr(new_instance, element, dictionary[element])
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Creates an instance of the calling class
        with the attributes passed in dictionary
        """
        try:
            with open("{}.json".format(cls.__name__), 'r') as f:
                objs = cls.from_json_string(f.read())
        except:
            objs = []
        list_ins = []
        for element in objs:
            list_ins += [cls.create(**element)]
        return list_ins
