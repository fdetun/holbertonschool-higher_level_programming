#!/usr/bin/python3
"""task 1"""
import urllib.request as request


if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as s:
        r = s.info()
        print(r['X-Request-Id'])
