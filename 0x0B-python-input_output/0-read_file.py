#!/usr/bin/python3
"""ReadFile module"""


def read_file(filename=""):
    with open(filename, encoding='utf8') as textfile:
        fde = textfile.read()
    print(fde)
