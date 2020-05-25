#!/usr/bin/python3
"""
 "5-text_indentation" module.
"""


def text_to_array(text):
    """
    text_to_array
    Args:
        text : string
    Returns:
        liss
    """
    delim = ".:?"
    a = 0
    liss = []
    new = []

    for f in range(0, (len(text))):
        if text[f] in delim:
            liss.append(text[a:f + 1])
            a = f + 1
    if text[:-1] not in delim:
        liss.append(text[a:len(text)])
    fil = filter(lambda ok: ok != "", liss)
    new = list(fil)
    return new


def text_indentation(text):
    """
    text_indentation
    Args:
        text : string
    Returns:
        None
    """
    inc = 0
    if not type(text) is str:
        raise TypeError("text must be a string")
    liss = text_to_array(text)
    for i in liss:
        if inc < len(liss) - 1:
            print("{}".format(i.strip()))
            print()
        else:
            print("{}".format(i.strip()), end="")
        inc = inc + 1
