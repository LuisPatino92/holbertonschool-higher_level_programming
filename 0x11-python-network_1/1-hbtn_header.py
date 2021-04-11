#!/usr/bin/python3
"""This module has a function that makes a request"""


import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io') as url_r:
        print(url_r.info()["X-Request-Id"])
