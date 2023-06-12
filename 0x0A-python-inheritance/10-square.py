#!/usr/bin/python3
"""module for square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size__ = size

    def area(self):
        """returns square area"""
        return self.__size__ * self.__size__

    def __str__(self):
        """returns printable string for rectangle"""
        return "[Square] {}/{}".format(self.__size__, self.__size__)
