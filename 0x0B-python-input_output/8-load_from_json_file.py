#!/usr/bin/python3
"""load_from_json_file module"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file python func
    args :
    my_obj
    filename
    """
    with open(filename, 'w') as jsonf:
        return json.load(jsonf)
