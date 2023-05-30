#!/usr/bin/python3
"""This is a simple square module"""


class Square:
    """A Square Class."""
    __size = 0
    """Set the class size attribute"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of the square"""
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print("\n".format())
        else:
            for i in range(0, self.size):
                for j in range(0, self.size):
                    print("#".format(), end="")
                print("".format(), end="\n")
