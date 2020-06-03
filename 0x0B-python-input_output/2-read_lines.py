#!/usr/bin/python3
"""read_lines"""


def read_lines(filename="", nb_lines=0):
    """
    read_lines
    args:
    filename=""
    nb_lines = int
    """
    with open(filename, encoding='utf8') as txtfile:
        if nb_lines > 0:
            for i in range(nb_lines):
                fde = txtfile.readline()
                print(fde, end="")
        else:
            for i in txtfile.readlines():
                print(i, end="")
