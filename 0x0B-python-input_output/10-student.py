#!/usr/bin/python3
"""module declares a student class"""


class Student:
    """a student class"""

    def __init__(self, first_name, last_name, age):
        """instatiates student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets dictionary of instance"""
        if attrs is None:
            return self.__dict__
        my_dict = {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return my_dict
