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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
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
            f.write(cls.to_json_string(list_dicts))

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
        cls.update(new_instance, **dictionary)
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of instances to a file in CSV format"""

        csv_str = ""
        for element in list_objs:
            csv_str += str(element.id) + ","
            if cls.__name__ == "Square":
                csv_str += str(element.size) + ","
            elif cls.__name__ == "Rectangle":
                csv_str += str(element.width) + ","
                csv_str += str(element.height) + ","
            csv_str += str(element.x) + ","
            csv_str += str(element.y) + "\n"
        with open("{}.csv".format(cls.__name__), 'w') as f:
            f.write(csv_str)

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of instances from a .csv file"""
        with open("{}.csv".format(cls.__name__), 'r') as f:
            csv_string = f.read()
        csv_lines = csv_string.split('\n')
        dict_obj = []
        for element in csv_lines[:-1]:
            csv_dict = {}
            if cls.__name__ == "Rectangle":
                csv_dict['id'] = int(element.split(',')[0])
                csv_dict['width'] = int(element.split(',')[1])
                csv_dict['height'] = int(element.split(',')[2])
                csv_dict['x'] = int(element.split(',')[3])
                csv_dict['y'] = int(element.split(',')[4])
            elif cls.__name__ == "Square":
                csv_dict['id'] = int(element.split(',')[0])
                csv_dict['size'] = int(element.split(',')[1])
                csv_dict['x'] = int(element.split(',')[2])
                csv_dict['y'] = int(element.split(',')[3])
            dict_obj += [cls.create(**csv_dict)]
        return dict_obj
