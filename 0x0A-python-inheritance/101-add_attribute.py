#!/usr/bin/python3
"""Module"""


def add_attribute(fde, names, values):
    """add_attribute"""
    if not hasattr(fde, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(fde, names, values)
