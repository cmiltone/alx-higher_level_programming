#!/usr/bin/python3
"""Unittest for Base class
"""


import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test Cases for Base class"""
    # def test_for_correctness(self):
    #     b1 = Base()
    #     self.assertEqual(1, b1.id)
    #     b2 = Base()
    #     self.assertEqual(2, b2.id)
    #     b3 = Base()
    #     self.assertEqual(3, b3.id)
    #     b4 = Base(13)
    #     self.assertEqual(13, b4.id)
    #     b4 = Base()
    #     self.assertEqual(4, b5.id)
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
        b4 = Base()
        self.assertEqual(2, b5.id)