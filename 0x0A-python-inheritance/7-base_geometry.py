#!/usr/bin/python3
"""module declares class BaseGeometry and Rectangle"""


class BaseGeometry:
    """a BaseGeometry class"""
    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise TypeError(name + " must be greater than 0")
