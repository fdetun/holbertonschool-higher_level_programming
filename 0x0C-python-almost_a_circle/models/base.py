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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        function return json string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        lst = []
        filename = str(cls.__name__) + ".json"
        if list_objs is None:
            lst = []
        else:
            for i in list_objs:
                lst.append(cls.to_dictionary(i))
        with open(filename, "w", encoding="utf-8") as fde:
            fde.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
