#!/usr/bin/python3
"""This module has the save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """Receives an object and writes its JSON representation in a file"""

    data = json.dumps(my_obj)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)
