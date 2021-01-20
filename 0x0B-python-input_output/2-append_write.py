#!/usr/bin/python3
"""This module has the append_write function"""


def append_write(filename="", text=""):
    """Writes in a file (appends if exists, creates if don't

    Args:
        filename (string):      The path of the file to write in
        text (string):          The string to be written

    Returns the amount of chars written
    """

    written_chars = 0

    with open(filename, 'a', encoding='utf-8') as f:
        written_chars += f.write(text)

    return written_chars
