#!/usr/bin/python3
"""task10"""
import requests
import sys

if __name__ == "__main__":
    uname = sys.argv[1]
    token = "2f0ff6a39beb16e93baef22b146fb6dd10e0903d"
    api = "https://api.github.com/repos/"
    url = api + uname + "/" + sys.argv[2] + "/commits"
    login = requests.get(url, auth=(uname, token))
    f = login.json()
    for i in range(10):
        a = f[i]["sha"]
        b = f[i]["commit"]["author"]["name"]
        print("{} {}".format(a, b))
