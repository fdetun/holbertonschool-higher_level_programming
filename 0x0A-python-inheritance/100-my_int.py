#!/usr/bin/python3
"""Myint"""


class MyInt(int):
    """ class MyInt """

    def __eq__(self, fd):
        """equal"""
        return int(self) != int(fd)

    def __ne__(self, fde):
        """not equal"""
        return int(self) == int(fde)
