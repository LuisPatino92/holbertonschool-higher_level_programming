#!/usr/bin/python3
"""unitary test for Base Class"""


from models import base
import unittest
import pep8

Base = base.Base


class BaseTests(unittest.TestCase):
    """Tests for Base class"""

    def test_module_docs(self):
        """Test for module docstring"""
        self.assertTrue(len(base.__doc__) > 1)

    def test_class_docs(self):
        """Test for Base docstring"""
        self.assertTrue(len(base.Base.__doc__) > 1)

    def test_pep8_main_file(self):
        """Test pep8 ok."""
        r = pep8.StyleGuide().check_files(['models/base.py'])
        self.assertEqual(r.total_errors, 0, "Pep8 issues Found.")

    def test_pep8_test(self):
        """Test pep8 ok."""
        r = pep8.StyleGuide().check_files(['tests/test_models/test_base.py'])
        self.assertEqual(r.total_errors, 0, "Pep8 issues Found.")

    def test_correct_id(self):
        """Checks if Base is handling _nb_objects OK"""
        b1 = Base()
        b2 = Base(56)
        b3 = Base()

        self.assertTrue(b1.id == 1)
        self.assertTrue(b2.id == 56)
        self.assertTrue(b3.id == 2)


if __name__ == "__main__":
    unittest.main()
