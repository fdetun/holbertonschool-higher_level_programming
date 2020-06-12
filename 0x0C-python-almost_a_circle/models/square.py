#!/usr/bin/python3
"""Rectangle Class File"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Rectangle Class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update function
        """
        ar = ["id", "size", "x", "y"]
        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, ar[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        update dict
        """
        arr = ["id", "size", "x", "y", ]
        return dict([(x, getattr(self, x)) for x in arr])
