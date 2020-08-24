#!/usr/bin/python3
"""task10"""
import requests
import sys

if __name__ == "__main__":
    uname = sys.argv[1]
    api = "https://api.github.com/repos/"
    url = api + uname + "/" + sys.argv[2] + "/commits"
    login = requests.get(url)
    f = login.json()
    for i in range(10):
        a = f[i]["sha"]
        b = f[i]["commit"]["author"]["name"]
        print("{} {}".format(a, b))
