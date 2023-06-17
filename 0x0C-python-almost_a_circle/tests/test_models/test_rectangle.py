#!/usr/bin/python3
"""Unittest for Rectangle class
"""


import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test Cases for Rectangle class"""
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

    def test_for_invalid_width_value(self):
        with self.assertRaises(Exception) as context:
            r = Rectangle(-1, 2)
        self.assertTrue("width must be >= 0" == str(context.exception))

    def test_for_invalid_width_type(self):
        with self.assertRaises(Exception) as context:
            r = Rectangle("10", 2)
        self.assertTrue("width must be an integer" == str(context.exception))

    def test_for_invalid_height_value(self):
        with self.assertRaises(Exception) as context:
            r = Rectangle(1, -2)
        self.assertTrue("height must be >= 0" == str(context.exception))

    def test_for_invalid_height_type(self):
        with self.assertRaises(Exception) as context:
            r = Rectangle(10, "2")
        self.assertTrue("height must be an integer" == str(context.exception))

    def test_for_invalid_x_value(self):
        with self.assertRaises(Exception) as context:
            r = Rectangle(1, 2, -1)
        self.assertTrue("x must be >= 0" == str(context.exception))
    
    def test_for_invalid_x_type(self):
        with self.assertRaises(Exception) as context:
            r = Rectangle(10, 2, "2")
        self.assertTrue("x must be an integer" == str(context.exception))
    
    def test_for_invalid_y_value(self):
        with self.assertRaises(Exception) as context:
            r = Rectangle(1, 2, 4, -1)
        self.assertTrue("y must be >= 0" == str(context.exception))
    
    def test_for_invalid_y_type(self):
        with self.assertRaises(Exception) as context:
            r = Rectangle(10, 2, 1, "2")
        self.assertTrue("y must be an integer" == str(context.exception))