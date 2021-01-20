#!/usr/bin/python3
"""This module has the load_from_json_file function"""


import json


def load_from_json_file(filename):
    """Charges the json of and object and returns it"""

    jason_str = ""

    with open(filename, 'r', encoding='utf-8') as f:
        jason_str = f.read()

    return json.loads(jason_str)
