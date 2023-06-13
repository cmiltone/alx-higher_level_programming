#!/usr/bin/python3
"""
module gets an object represented by a JSON string
"""
import json
from io import StringIO


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    io = StringIO(my_str)
    return json.load(io)
