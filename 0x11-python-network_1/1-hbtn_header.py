#!/usr/bin/python3
"""This module has a function that makes a request"""


import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as url_r:
        print(url_r.info()["X-Request-Id"])
