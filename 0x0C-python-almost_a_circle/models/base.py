#!/usr/bin/python3
"""Base Class File"""
import json


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init func
        args:
        id (int)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        function return json string
        """
        if list_dictionaries is None:
            fdetun = "{}".format('"[]"')
        else:
            fdetun = json.dumps(list_dictionaries)
        return fdetun
