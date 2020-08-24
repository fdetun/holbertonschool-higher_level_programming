#!/usr/bin/python3
"""task8"""
import requests
import sys

if __name__ == "__main__":
    URL = "http://19.hbtn-cod.io:5000/search_user"
    ar = ""
    if sys.argv[1]:
        ar = sys.argv[1]
    p = requests.post(URL, {"q": ar})
    try:
        f = p.json()
        if f:
            print("[{}] {}".format(f.get("id"), f.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
