#!/usr/bin/python3
"""module to create object  from json file"""
import json
from io import StringIO


def load_from_json_file(filename):
    """creates object  from json file"""
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        io = StringIO(data)
        obj = json.load(io)
    return obj
