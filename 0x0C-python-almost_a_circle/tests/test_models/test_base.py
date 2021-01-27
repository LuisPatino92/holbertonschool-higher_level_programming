#!/usr/bin/python3
"""unitary test for Base Class"""


import unittest
import pep8


class BaseTests(unittest.TestCase):
    """Tests for Base class"""

    def test_pep8_main_file(self):
        """Test pep8 ok."""
        """Test pep8 ok."""
        r = pep8.StyleGuide().check_files(['models/base.py'])
        self.assertEqual(r.total_errors, 0, "Pep8 issues Found.")

    def test_pep8_test(self):
        """Test pep8 ok."""
        r = pep8.StyleGuide().check_files(['tests/test_models/test_base.py'])
        self.assertEqual(r.total_errors, 0, "Pep8 issues Found.")

if __name__ == "__main__":
    unittest.main()
