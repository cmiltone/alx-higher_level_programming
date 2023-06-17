#!/usr/bin/python3
"""(self, width, height, x=0, y=0, id=None)
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
        h = self.height
        return "[Square] ({}) {}/{} - {}/{}".format(id, x, y, w, h)
