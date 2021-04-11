#!/usr/bin/python3
"""This module has a function that makes a request"""


import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as url_r:
        response = url_r.read()
        print("Body response:")
        print("\t- {}".format(type(response)))
        print("\t- {}".format(response))
        print("\t- {}".format(str(response, 'utf-8')))
