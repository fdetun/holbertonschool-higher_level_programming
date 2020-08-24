#!/usr/bin/python3
"""task4"""
import requests
import sys

if __name__ == "__main__":
    payload = {"email": sys.argv[2]}
    URL = sys.argv[1]
    p = requests.post(URL, payload)
    print(p.text)
