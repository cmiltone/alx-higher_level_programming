#!/usr/bin/python3
"""module opens a file and appends to it"""


def append_write(filename="", text=""):
    """appends text to a file"""
    with open(filename, "a+") as f:
        chars = f.write(text)
    return chars
