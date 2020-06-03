#!/usr/bin/python3
"""write_file python script"""


def write_file(filename="", text=""):
    """
    write_file func
    args:
    filename =""
    text = ""
    """
    with open(filename, 'w', encoding="utf8") as txtfile:
        fde = txtfile.write(text)
    return fde
