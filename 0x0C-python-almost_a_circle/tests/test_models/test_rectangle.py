#!/usr/bin/python3
"""Unittest for Rectangle class
"""


import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test Cases for Rectangle class"""
    # def test_for_correctness(self):
    #     b1 = Rectangle()
    #     self.assertEqual(1, b1.id)
    #     b2 = Rectangle()
    #     self.assertEqual(2, b2.id)
    #     b3 = Rectangle()
    #     self.assertEqual(3, b3.id)
    #     b4 = Rectangle(13)
    #     self.assertEqual(13, b4.id)
    #     b4 = Rectangle()
    #     self.assertEqual(4, b5.id)
    def test_for_correct_assignment(self):
        """Test for correct assignment"""
        b = Rectangle(10, 2)
        self.assertEqual(3, b.id)
    def test_for_correct_increment(self):
        """Test for correct increment"""
        b = Rectangle(2, 10)
        self.assertEqual(4, b.id)
        b4 = Rectangle(10, 2, 0, 0, 13)
        self.assertEqual(13, b4.id)
        b5 = Rectangle(2, 3)
        self.assertEqual(5, b5.id)