#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""module declares class Rectangle"""


class Rectangle(BaseGeometry):
    """a Rectangle class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height__ = height
        self.__width__ = width
