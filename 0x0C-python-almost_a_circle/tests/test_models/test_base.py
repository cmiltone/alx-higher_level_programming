#!/usr/bin/python3
"""Unittest for Base class
"""


import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test Cases for Base class"""

    def test_for_correct_assignment(self):
        """Test for correct assignment"""
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_for_correct_increment(self):
        """Test for correct increment"""
        b = Base()
        self.assertEqual(1, b.id)
        b4 = Base(13)
        self.assertEqual(13, b4.id)
        b5 = Base()
        self.assertEqual(2, b5.id)

    def test_to_json_string_method(self):
        b = Base(4)
        s = b.to_json_string({"id": 2})
        self.assertEqual('{"id": 2}', s)
