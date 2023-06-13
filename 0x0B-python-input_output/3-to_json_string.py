#!/usr/bin/python3
"""module gets json representation of an object"""
import json


def to_json_string(my_obj):
    """returns json representation of an object"""
    return json.dumps(my_obj)
