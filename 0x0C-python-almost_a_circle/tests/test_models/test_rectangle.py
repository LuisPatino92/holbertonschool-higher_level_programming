#!/usr/bin/python3
"""unitary test for Base Class"""

from models import rectangle
import unittest
import pep8


class RectangleTests(unittest.TestCase):
    """Tests for Base class"""

    def test_module_docs(self):
        """Test for module docstring"""
        self.assertTrue(len(rectangle.__doc__) > 1)

    def test_class_docs(self):
        """Test for Base docstring"""
        self.assertTrue(len(rectangle.Rectangle.__doc__) > 1)

    def test_pep8_main_file(self):
        """Test pep8 ok."""
        r = pep8.StyleGuide().check_files(['models/rectangle.py'])
        self.assertEqual(r.total_errors, 0, "Pep8 issues Found.")

    def test_pep8_test(self):
        """Test pep8 ok."""
        r = pep8.StyleGuide().check_files(
                ['tests/test_models/test_rectangle.py'])
        self.assertEqual(r.total_errors, 0, "Pep8 issues Found.")

if __name__ == "__main__":
    unittest.main()
