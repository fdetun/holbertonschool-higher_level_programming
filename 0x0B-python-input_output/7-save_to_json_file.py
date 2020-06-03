#!/usr/bin/python3
"""SaveToJsonFile module"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file python func
    args :
    my_obj
    filename
    """
    with open(filename, 'w') as jsonf:
        json.dump(my_obj, jsonf)
