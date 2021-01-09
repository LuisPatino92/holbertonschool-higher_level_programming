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

    splited = text.translate(breakers).split(chr(126))

    i = -1

    for i in range(len(splited) - 1):
        print(splited[i].lstrip().rstrip(), end="\n\n")
    print(splited[i + 1].lstrip().rstrip(), end="")
