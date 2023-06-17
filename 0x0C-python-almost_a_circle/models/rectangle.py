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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """ getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates and returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints the rectangle using #"""
        s = ""
        if self.height == 0 or self.width == 0:
            return s
        for i in range(self.height + self.y):
            if i < self.y:
                s += ""
            else:
                for j in range(self.width + self.x):
                    if j < self.x:
                        s = s + " "
                    else:
                        s = s + "#"
            if i < (self.height + self.y) - 1:
                s = s + "\n"
        print("{}".format(s))

    def __str__(self):
        id = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, w, h)
