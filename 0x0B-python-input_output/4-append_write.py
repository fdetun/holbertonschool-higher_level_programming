#!/usr/bin/python3
"""append_write python script"""


def append_write(filename="", text=""):
    """
    append_write func
    args:
    filename =""
    text = ""
    """
    with open(filename, 'a', encoding="utf8") as txtfile:
        fde = txtfile.write(text)
    return fde
