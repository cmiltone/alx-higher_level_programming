#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test Cases for max_integer function"""
    def test_for_empty_list(self):
        """Test for empty list"""
        self.assertEqual(None, max_integer([]))

    def test_for_correctness(self):
        """Test for correctness"""
        self.assertEqual(10, max_integer([3, 5, 6, 10, 2]))

    def test_for_negative_values(self):
        """Test for negative values"""
        self.assertEqual(4, max_integer([1, 2, 4, -7, -2]))

    def test_for_boolean_values(self):
        """Test for boolean values"""
        self.assertEqual(9, max_integer([1, 2, 4, False, 9, True]))
