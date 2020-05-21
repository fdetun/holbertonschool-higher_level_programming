#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """
    This is a class named square.

    Attributes:
        self (int): self.
        size (int): number.
    """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """ This is a new func! """
        a = self.__size
        return a ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """This is a function.

        Attributes:
        self (int): self.
        value (int): number.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
