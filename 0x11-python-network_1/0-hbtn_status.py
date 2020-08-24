#!/usr/bin/python3
"""task 0"""
import urllib.request

if __name__ == "__main__":
    resource = urllib.request.urlopen("https://intranet.hbtn.io/status")
    html = resource.read()
    print("Body response:")
    print("\t- type: {}".format(html.__class__))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode("utf-8")))
