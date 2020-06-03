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
    with open(filename, encoding='utf-8') as jsonf:
        return json.loads(jsonf.read())
