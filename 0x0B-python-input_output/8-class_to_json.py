#!/usr/bin/python3
"""module gets dictionary description of object"""


def class_to_json(obj):
    """gets dictionary description of object"""
    return obj.__dict__
