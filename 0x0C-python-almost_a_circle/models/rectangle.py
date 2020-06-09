#!/usr/bin/python3
"""Rectangle Class File"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init func
        args:
        id (int)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
