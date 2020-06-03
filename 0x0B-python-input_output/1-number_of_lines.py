#!/usr/bin/python3
"""number_of_lines file"""


def number_of_lines(filename=""):
    """
    number_of_lines func
    args:
    filename
    """
    count = 0
    with open(filename) as txtfile:
        for i in txtfile.readlines():
            count += 1
    return count
