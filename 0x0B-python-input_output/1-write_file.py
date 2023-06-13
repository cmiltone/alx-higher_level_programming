#!/usr/bin/python3
"""opens a file and writes to it"""


def write_file(filename="", text=""):
    with open(filename, "a+") as f:
        chars = f.write(text)
    return chars
