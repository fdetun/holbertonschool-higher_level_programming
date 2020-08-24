#!/usr/bin/python3
"""task5"""
import requests
import sys


URL = sys.argv[1]
s = requests.Session()
r = s.get(URL)
print(r.headers["X-Request-Id"])
