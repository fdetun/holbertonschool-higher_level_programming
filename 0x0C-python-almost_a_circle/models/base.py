#!/usr/bin/python3
"""Base Class File"""


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init func
        args:
        id (int)
        """
        if id is not None:
            self.id = int(id)
        Base.__nb_objects += 1
        self.id = self.__nb_objects
