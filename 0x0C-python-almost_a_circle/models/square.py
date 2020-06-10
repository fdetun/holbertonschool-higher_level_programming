#!/usr/bin/python3
"""Rectangle Class File"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Rectangle Class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))
