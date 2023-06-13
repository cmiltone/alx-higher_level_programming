#!/usr/bin/python3
"""module writes JSON representation of an object to file"""
import json


def save_to_json_file(my_obj, filename):
    """writes JSON representation of an object to file"""
    with open(filename, "w+") as f:
        json.dump(my_obj, f)
