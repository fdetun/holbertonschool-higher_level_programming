#!/usr/bin/python3
"""
lookup function
"""


def lookup(obj):
    """
    lookup
    """
    a = list(f for f in dir(obj))
    return a
