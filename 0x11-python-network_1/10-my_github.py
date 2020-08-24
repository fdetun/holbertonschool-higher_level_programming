#!/usr/bin/python3
"""task10"""
import requests
import sys

if __name__ == "__main__":
    uname = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/users/" + uname
    login = requests.get(url, auth=(uname, token))
    print(login.json().get("id"))
