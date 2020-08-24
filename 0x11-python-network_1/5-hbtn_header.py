#!/usr/bin/python3
"""task4"""
import requests
import sys

if __name__ == "__main__":
    URL = sys.argv[1]
    s = requests.Session()
    r = s.get(URL)
    print(r.headers["X-Request-Id"])
