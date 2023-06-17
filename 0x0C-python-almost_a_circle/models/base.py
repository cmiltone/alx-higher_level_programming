#!/usr/bin/python3
"""
module for base class
"""
import json


class Base:
    """sbase class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """set the id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json representation of the class"""
        if len(list_dictionaries) <= 0:
            return "[]"
        return json.dumps(list_dictionaries)

