#!/usr/bin/python3
"""task8"""
import requests
import sys

if __name__ == "__main__":
    URL = "http://0.0.0.0:5000/search_user"
    ar = ""
    if sys.argv[1]:
        ar = sys.argv[1]
    p = requests.post(URL, {"q": ar})
    try:
        f = p.json()
        if len(f) == 0:
            print("No result")
        else:
            print("[{}] {}".format(f["id"], f["name"]))
    except ValueError:
        print("Not a valid JSON")
