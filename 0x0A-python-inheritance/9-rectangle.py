#!/usr/bin/python3
"""
class Rectangle that inherits a class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """inisialisation of a rectangle class"""
        self.integer_validator("width", width)
        self._wh = width
        self.integer_validator("height", height)
        self._ht = height

    def area(self):
        return self._wh * self._ht

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self._wh, self._ht)
