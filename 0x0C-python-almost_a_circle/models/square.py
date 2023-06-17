#!/usr/bin/python3
"""
module for square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """sets size, x, y and id"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns square printable string"""
        id = self.id
        x = self.x
        y = self.y
        w = self.width
        return "[Square] ({}) {}/{} - {}".format(id, x, y, w)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value
