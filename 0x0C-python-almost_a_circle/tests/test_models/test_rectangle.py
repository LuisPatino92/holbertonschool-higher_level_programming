#!/usr/bin/python3
"""unitary test for Base Class"""

from models import rectangle
from models import base
import unittest
import pep8

Base = base.Base
Rectangle = rectangle.Rectangle


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

    def test_id_mechanism(self):
        """Checks if id mechanism was inherited OK"""
        r1 = Rectangle(9, 9)
        b1 = Base(10)
        r2 = Rectangle(9, 9)
        b2 = Base()

        self.assertEqual(r1.id, 3)
        self.assertEqual(b1.id, 10)
        self.assertEqual(r2.id, 4)
        self.assertEqual(b2.id, 3)

if __name__ == "__main__":
    unittest.main()
