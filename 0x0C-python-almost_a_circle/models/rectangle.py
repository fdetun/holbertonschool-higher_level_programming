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
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter function
        """
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter function
        """
        self.__height = value

    @property
    def x(self):
        """
        x getter function
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter function
        """
        self.__x = value

    @property
    def y(self):
        """
        x getter function
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter function
        """
        self.__y = value
