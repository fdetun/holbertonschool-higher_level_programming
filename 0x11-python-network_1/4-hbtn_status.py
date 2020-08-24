#!/usr/bin/python3
"""task4"""
import requests


URL = "https://intranet.hbtn.io/status"
s = requests.Session()
r = s.get(URL)
print("Body response:")
print("\t- type: {}".format(r.text.__class__))
print("\t- content: {}".format(r.text))
