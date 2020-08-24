#!/usr/bin/python3
"""task 3"""
import urllib.request as request
import urllib.parse as parse
import sys


if __name__ == "__main__":
    data = parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    with request.urlopen(sys.argv[1], data) as s:
        print(s.read().decode('utf-8'))
