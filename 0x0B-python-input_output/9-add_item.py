#!/usr/bin/python3
"""add item module"""
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
try:
    fde = load_from_json_file("add_item.json")
except:
    fde = []
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        fde.append(sys.argv[i])
save_to_json_file(fde, "add_item.json")
