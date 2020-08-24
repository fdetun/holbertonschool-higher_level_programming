#!/usr/bin/python3
"""task 0"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as resource:
        html = resource.read()
        print("Body response:")
        print("\t- type: {}".format(html.__class__))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
