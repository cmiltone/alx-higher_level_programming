#!/usr/bin/python3
"""This is a simple square module"""


class Square:
    """A Square Class."""
    __size = 10
    """Set the class size attribute"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for size"""
        if not isinstance(size, int) and not isinstance(size, float):
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of the square"""
        return self.__size * self.__size

    def __eq__(self, other):
        """Checks for equality"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks for not equal"""
        return self.area() != other.area()
    
    def __le__(self, other):
        """Checks for less than or equal to"""
        return self.area() <= other.area()
    
    def __lt__(self, other):
        """Checks for less than"""
        return self.area() < other.area()

    def __gt__(self, other):
        """Checks for greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks for greater than or equal to"""
        return self.area() >= other.area()
