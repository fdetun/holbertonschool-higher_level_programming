#!/usr/bin/python3
"""task 3"""
from urllib.request import Request, urlopen
import urllib.parse as parse
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    f = Request(sys.argv[1])
    try:
        with urlopen(f) as s:
            print(s.read().decode('utf-8'))
    except HTTPError as r:
        print('Error code: ', r.code)
