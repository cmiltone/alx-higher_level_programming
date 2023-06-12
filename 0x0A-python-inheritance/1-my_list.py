#!/usr/bin/python3
""" module to inherit from list"""


class MyList(list):
    """ inherits from list"""
    __list__ = []

    def print_sorted(self):
        """ prints sorted list items"""
        ints = self.copy()
        ints.sort()
        print(ints)
