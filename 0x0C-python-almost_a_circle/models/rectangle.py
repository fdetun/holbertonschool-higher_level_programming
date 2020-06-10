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

    def CheckSet(self, var, value):
        """
        check Type Function
        Args:
        var
        value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(var))
        if var == "width" or var == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(var))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(var))

    @property
    def width(self):
        """width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter function
        """
        self.CheckSet("width", value)
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
        self.CheckSet("height", value)
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
        self.CheckSet("x", value)
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
        self.CheckSet("y", value)
        self.__y = value

    def area(self):
        """
        area function
        """
        return self.width * self.height

    def display(self):
        """
        display function
        """
        for i in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """
        str Function
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))
