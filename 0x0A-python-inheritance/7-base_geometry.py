#!/usr/bin/python3
"""
class BaseGeometry
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
