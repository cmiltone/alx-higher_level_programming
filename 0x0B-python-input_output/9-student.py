#!/usr/bin/python3
"""module declares a student class"""


class Student:
    """a student class"""

    def __init__(self, first_name, last_name, age):
        """instatiates student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """gets dictionary of instance"""
        return self.__dict__
