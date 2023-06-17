#!/usr/bin/python3
"""
module for rectanlge class
"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ sets width, height, x, y and id"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ getter for width"""
        return __width

    @width.setter
    def width(self, width):
        """setter for width"""
        self.__width = width

    @property
    def height(self):
        """ getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter for height"""
        self.__height = height

    @property
    def x(self):
        """ getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for x"""
        self.__x = x

    @property
    def y(self):
        """ getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for y"""
        self.__y = y
        