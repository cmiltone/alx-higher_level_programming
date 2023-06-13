#!/usr/bin/python3
""""module to read and print contents of file"""


def read_file(filename=""):
    """reads file and prints the content"""
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
