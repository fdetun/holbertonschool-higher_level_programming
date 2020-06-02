#!/usr/bin/python3
"""
inherits_from
"""


def inherits_from(obj, a_class):
    """
    Returns True or false
    """
    return (isinstance(obj, a_class) and not (type(obj) is a_class))
