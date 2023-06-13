#!/usr/bin/python3
"""module opens a file and writes to it"""


def write_file(filename="", text=""):
    """writes text to a file"""
    with open(filename, "w+") as f:
        chars = f.write(text)
    return chars
