#!/usr/bin/python3
"""unitary test for Base Class"""

from models import square
from models import rectangle
from models import base
import unittest
import pep8

Base = base.Base
Rectangle = rectangle.Rectangle
Square = square.Square


class SquareTests(unittest.TestCase):
    """Tests for Base class"""

    def test_module_docs(self):
        """Test for module docstring"""
        self.assertTrue(len(square.__doc__) > 1)

    def test_class_docs(self):
        """Test for Base docstring"""
        self.assertTrue(len(square.Square.__doc__) > 1)

    def test_pep8_main_file2(self):
        """Test pep8 ok."""
        """Test pep8 ok."""
        r = pep8.StyleGuide().check_files(['models/square.py'])
        self.assertEqual(r.total_errors, 0, "Pep8 issues Found.")

    def test_pep8_test(self):
        """Test pep8 ok."""
        r = pep8.StyleGuide().check_files(['tests/test_models/test_square.py'])
        self.assertEqual(r.total_errors, 0, "Pep8 issues Found.")

if __name__ == "__main__":
    unittest.main()
