#!/usr/bin/python3
"""This module has the to_json_string function"""

import json

def to_json_string(my_obj):
    """Receives an object and returns its JSON representation"""

    data = json.dumps(my_obj)
    return data
