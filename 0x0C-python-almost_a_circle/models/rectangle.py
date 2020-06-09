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
        
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
