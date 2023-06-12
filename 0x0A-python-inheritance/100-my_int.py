#!/usr/bin/python3
"""module for MyInt class that is based on int"""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, other):
        """change == to !="""
        return self.real != other

    def __ne__(self, other):
        """change != to =="""
        return self.real == other
