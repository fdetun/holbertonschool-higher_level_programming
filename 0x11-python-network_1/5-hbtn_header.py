#!/usr/bin/python3
"""task5"""
import requests
import sys


URL = sys.argv[1]
r = requests.get(URL)
print("{}".format(r.headers.get('X-Request-Id')))
