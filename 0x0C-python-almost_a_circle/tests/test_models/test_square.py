#!/usr/bin/python3
"""Unittest for Square class
"""


import unittest
from models.square import Square


class TestSqaureClass(unittest.TestCase):
    """Test Cases for Square class"""

    def test_for_correct_assignment(self):
        """Test for correct assignment"""
        s = Square(10, 2, 1, 2)
        self.assertEqual(2, s.id)

    def test_for_correct_size_getter_setter(self):
        """Test for correct size getter/setter"""
        s = Square(10, 3, 1, 3)
        s.size = 9
        self.assertEqual(9, s.size)

    def test_for_invalid_size_value(self):
        """Test for validity of size value check"""
        with self.assertRaises(Exception) as context:
            s = Square(1, 2, 4)
            s.size = -1
        self.assertTrue("width must be >= 0" == str(context.exception))

    def test_for_invalid_size_type(self):
        """Test for validity of size type check"""
        with self.assertRaises(Exception) as context:
            s = Square(10)
            s.size = "10"
        self.assertTrue("width must be an integer" == str(context.exception))

    def test_update_method_correctness(self):
        s = Square(4, 6, 2, 1)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", s.__str__())

    def test_update_method_correctness_with_kwars(self):
        s = Square(4, 6, 2, 1)
        s.update(x=1, size=2, y=3)
        self.assertEqual("[Square] (1) 1/3 - 2", s.__str__())

    def test_to_dictionary_method_correctness(self):
        s = Square(10, 2, 1, 1)
        obj = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(obj, s.to_dictionary())
