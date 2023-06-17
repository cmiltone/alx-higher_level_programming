#!/usr/bin/python3
"""
module for base class
"""
import json
from io import StringIO

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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        for item in list_objs:
            filename = item.__class__.__name__ + ".json"
            with open(filename, "w+") as f:
                f.write(cls.to_json_string([item.to_dictionary()]))

    @staticmethod
    def from_json_string(json_string):
        """returns an object represented by a JSON string"""
        io = StringIO(json_string)
        return json.load(io)
