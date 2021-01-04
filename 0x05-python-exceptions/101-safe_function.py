#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    res = ""
    try:
        res = fct(*args)
    except Exception as Err:
        sys.stderr.write("Exception: {}\n".format(Err))
        return None
    return res
