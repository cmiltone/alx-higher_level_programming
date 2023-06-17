#!/usr/bin/python3
"""Unittest for Square class
"""


import unittest
from models.square import Square


class TestSqaureClass(unittest.TestCase):
    """Test Cases for Square class"""

    def test_for_correct_assignment(self):
        """Test for correct assignment"""
        b = Square(10, 2, 1, 2)
        self.assertEqual(2, b.id)