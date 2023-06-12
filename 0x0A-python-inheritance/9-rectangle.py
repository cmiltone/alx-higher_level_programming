#!/usr/bin/python3
"""module declares class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a Rectangle class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height__ = height
        self.__width__ = width

    def area(self):
        """returns rectangle area"""
        return self.__height__ * self.__width__

    def __str__(self):
        """returns printable string for rectangel"""
        return "[Rectangle] {}/{} ".format(self.__width__, self.__height__)
