#!/usr/bin/python3
"""This module has the add attribute function"""


def add_attribute(obj, attr, value):
    """Function that adds an attribute to an object if it is possible
    Args:
        obj:     The object to add the attribute in
        attr:       The attribute
        value:      The value to be asigned to the attribute
    """

    if "__dict__" not in dir(type(obj)):
        raise TypeError("can't add new attribute ")

    obj.__dict__[attr] = value
