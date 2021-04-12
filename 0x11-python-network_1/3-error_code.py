#!/usr/bin/python3
"""This module has a function that makes a request"""


import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as url_r:
            response = url_r.read()
            print(str(response, 'utf-8'))
    except urllib.error.HTTPError:
        print("Error code: {}".format(sys.exc_info()[1].code))
