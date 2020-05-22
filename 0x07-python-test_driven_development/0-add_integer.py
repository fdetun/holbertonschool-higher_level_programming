#!/usr/bin/python3
"""
Add integer module
"""


def add_integer(a, b=98):
    """
    Add two integer a and b
    Args:
        a : the first number
        b : the second number
    Returns:
        sum
    """

    checkType = [int, float]
    if not type(a) in checkType:
        raise TypeError("a must be an integer")
    if not type(b) in checkType:
        raise TypeError("b must be an integer")
    else:
        sum = int(a) + int(b)
        return sum
