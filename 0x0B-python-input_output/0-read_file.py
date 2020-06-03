#!/usr/bin/python3
"""ReadFile file"""


def read_file(filename=""):
    """
    read file func
    args:
    filename
    """
    with open(filename, encoding='utf8') as textfile:
        fde = textfile.read()
    print(fde, end="")
