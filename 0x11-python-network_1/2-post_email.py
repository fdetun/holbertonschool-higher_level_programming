#!/usr/bin/python3
"""task 3"""
import urllib.request as request
import urllib.parse as parse
import sys

if __name__ == "__main__":
    data = parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    with request.urlopen(sys.argv[2], data) as s:
        print(s.read().decode('utf-8'))
