#!/usr/bin/python3
"""
class Square that inherits a class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Sqaure class"""
    def __init__(self, size):
        """init func of a Square class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self._fde = size

    def area(self):
        return (self._fde ** 2)
