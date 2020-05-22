#!/usr/bin/python3
"""
 3-say_my_name module
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name it is a function to print my name :D
    Args:
        first_name : the first number
        last_name : the second number
    Returns:
        None
    """

    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
