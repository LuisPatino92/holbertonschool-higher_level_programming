#!/usr/bin/python3
"""This module has the class_to_json function"""


import json


def class_to_json(obj):
    """Returns the dictionary description for JSON of an object"""

    serial = json.loads(json.dumps(obj.__dict__))

    return serial
