#!/usr/bin/python3
"""This is a simple square module"""


class Square:
    """A Square Class."""
    __size = 0
    __position = (0, 0)
    """Set the class size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in position:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Returns area of the square"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("\n".format())
        else:
            for i in range(0, self.__size):
                if self.position[1] <= 0:
                    for k in range(0, self.position[0]):
                        print(" ".format(), end="")
                for j in range(0, self.__size):
                    print("#".format(), end="")
                print("".format(), end="\n")
