#!/usr/bin/python3
"""This module has the text_indentation() function"""


def text_indentation(text):
    """ Function that takes a string and inserts two new lines

    Args:
        text:   Is the text to be indented.

        Indentation process consist in insert two new line
        after each "." "?" and ":"
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    breakers = {
                ord("."): "." + chr(126),
                ord("?"): "?" + chr(126),
                ord(":"): ":" + chr(126)}

    for line in text.translate(breakers).split(chr(126)):
        print(line.lstrip().rstrip(), end="\n\n")
