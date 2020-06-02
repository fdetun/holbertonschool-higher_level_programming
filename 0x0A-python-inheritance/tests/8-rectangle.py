#!/usr/bin/python3
"""
class Rectangle that inherits a class
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Area public instance"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(str(name)))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(str(name)))


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """inisialisation of a rectangle class"""
        self.integer_validator("width", width)
        self._wh = width
        self.integer_validator("height", height)
        self._ht = height
