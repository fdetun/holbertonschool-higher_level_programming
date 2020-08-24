#!/usr/bin/python3
"""task8"""
import requests
import sys

if __name__ == "__main__":
    URL = "http://0.0.0.0:5000/search_user"
    ar = ""
    if len(sys.argv) > 1:
        ar = sys.argv[1]
    p = requests.post(URL, {"q": ar})
    try:
        f = p.json()
        if len(f) > 0:
            print("[{}] {}".format(f["id"], f["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
