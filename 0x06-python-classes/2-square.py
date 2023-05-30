#!/usr/bin/python3
"""This is a simple square module"""


class Square:
    """A Square Class."""
    __size = 10
    """Set the class size attribute"""
    def __init__(self, size = 0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
