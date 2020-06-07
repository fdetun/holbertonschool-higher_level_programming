#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """append_after Function
    Args:
        filename: filename
        search_string: search_string
        new_string: new_string
    """
    with open(filename, "r", encoding="utf-8") as txtfile:
        buffer = ""
        for line in txtfile:
            buffer += line
            if search_string in line:
                buffer = buffer + new_string

    with open(filename, mode='w', encoding='utf-8') as fde:
        fde.write(buffer)
