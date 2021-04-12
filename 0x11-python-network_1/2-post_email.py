#!/usr/bin/python3
"""This module has a function that makes a request"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    data = parse.urlencode({"email": sys.argv[2]}).encode()
    req = request.Request(sys.argv[1], data=data)
    with request.urlopen(req) as response:
        print(str(response.read(), "utf-8"))
