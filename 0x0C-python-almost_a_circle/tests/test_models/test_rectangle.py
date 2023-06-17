#!/usr/bin/python3
"""Unittest for Rectangle class
"""


import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test Cases for Rectangle class"""

    def test_for_correct_assignment(self):
        """Test for correct assignment"""
        b = Rectangle(10, 2, 1, 2, 3)
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
        """Test for validity of width value check"""
        with self.assertRaises(Exception) as context:
            r = Rectangle(-1, 2)
        self.assertTrue("width must be >= 0" == str(context.exception))

    def test_for_invalid_width_type(self):
        """Test for validity of width type check"""
        with self.assertRaises(Exception) as context:
            r = Rectangle("10", 2)
        self.assertTrue("width must be an integer" == str(context.exception))

    def test_for_invalid_height_value(self):
        """Test for validity of height value check"""
        with self.assertRaises(Exception) as context:
            r = Rectangle(1, -2)
        self.assertTrue("height must be >= 0" == str(context.exception))

    def test_for_invalid_height_type(self):
        """Test for validity of height type check"""
        with self.assertRaises(Exception) as context:
            r = Rectangle(10, "2")
        self.assertTrue("height must be an integer" == str(context.exception))

    def test_for_invalid_x_value(self):
        """Test for validity of x value check"""
        with self.assertRaises(Exception) as context:
            r = Rectangle(1, 2, -1)
        self.assertTrue("x must be >= 0" == str(context.exception))
    
    def test_for_invalid_x_type(self):
        """Test for validity of x type check"""
        with self.assertRaises(Exception) as context:
            r = Rectangle(10, 2, "2")
        self.assertTrue("x must be an integer" == str(context.exception))
    
    def test_for_invalid_y_value(self):
        """Test for validity of y value check"""
        with self.assertRaises(Exception) as context:
            r = Rectangle(1, 2, 4, -1)
        self.assertTrue("y must be >= 0" == str(context.exception))
    
    def test_for_invalid_y_type(self):
        """Test for validity of y type check"""
        with self.assertRaises(Exception) as context:
            r = Rectangle(10, 2, 1, "2")
        self.assertTrue("y must be an integer" == str(context.exception))

    def test_area_method_correctness(self):
        r = Rectangle(10, 5)
        self.assertEqual(10 * 5, r.area())

    # def test_display_method_correctness(self):
    #     r = Rectangle(4, 6)
    #     s = "####\n####\n####\n####\n####\n####"
    #     self.assertEqual(s, r.display())

    def test_str_method_correctness(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual("[Rectangle] (12) 2/1 - 4/6", r.__str__())

    def test_update_method_correctness(self):
        r = Rectangle(4, 6, 2, 1, 12)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", r.__str__())

    def test_update_method_correctness_with_kwars(self):
        r = Rectangle(4, 6, 2, 1, 12)
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (12) 1/3 - 4/2", r.__str__())

    def test_to_dictionary_method_correctness(self):
        r = Rectangle(10, 2, 1, 9, 1)
        obj = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(obj, r.to_dictionary())
