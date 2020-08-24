#!/usr/bin/python3
"""task4"""
import requests
import sys

if __name__ == "__main__":
    URL = sys.argv[1]
    p = requests.get(URL)
    if p.status_code >= 400:
        print("Error code: {}".format(p.status_code))
