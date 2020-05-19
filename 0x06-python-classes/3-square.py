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
        """This is a function.

        Attributes:
        self (int): self.
        size (int): number.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__fd = size

    def area(self):
        """ This is a new func! """
        a = self.__fd
        return a ** 2
