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
        s = self.size
        return "[Square] ({}) {}/{} - {}".format(id, x, y, s)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]

        if len(args) <= 0:
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
