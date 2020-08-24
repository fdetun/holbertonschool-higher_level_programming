#!/usr/bin/python3
"""task4"""
import requests
import sys

if __name__ == "__main__":
    URL = sys.argv[1]
    r = requests.get(URL)
    print(r.headers.get("X-Request-Id"))
