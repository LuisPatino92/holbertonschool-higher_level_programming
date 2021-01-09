#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Tests when a correct list is passed
        self.assertEqual(max_integer([-1000, -2, -5699]), -2)
        self.assertEqual(max_integer([1, -2, 10, 5]), 10)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1000]), -1000)
        self.assertEqual(max_integer([1, -2, 3, -4, 5, -6, 7, -8, 9, 10, -152, 2, 2, 588]), 588)
        self.assertEqual(max_integer([x for x in range(-40, 500, 2)]), 498)
