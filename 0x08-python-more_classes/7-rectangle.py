#!/usr/bin/python3
"""module defines a rectangle class"""


class Rectangle:
    """ a rectangle class"""
    __height = None
    __width = None

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize rectangle"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for width"""
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
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ computes rectangle area and returns it"""
        return self.__height * self.__width

    def perimeter(self):
        """ computes rectangle perimeter and returns it"""
        return (self.__height + self.__width) * 2

    def __str__(self):
        s = ""
        if self.__height == 0 or self.__width == 0:
            return s
        for i in range(self.__height):
            for j in range(self.__width):
                s = s + str(self.print_symbol)
            if i < self.__height - 1:
                s = s + "\n"
        return s

    def __repr__(self):
        s = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return s

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
