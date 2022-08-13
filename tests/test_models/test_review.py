#!/usr/bin/python3
""" Unit tests for Review class """

import unittest
from models.review import Review
import pep8


class Test_Review(unittest.TestCase):
    """Base class tests"""

    def test_pep8_conformance_review(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_hasattr(self):
        """ Test if an object has an attribute """
        rev = Review()
        self.assertTrue(hasattr(rev, "place_id"))
        self.assertTrue(hasattr(rev, "user_id"))
        self.assertTrue(hasattr(rev, "text"))

    def test_type_review(self):
        """ Test the type of the attribute """
        rev = Review()
        self.assertEqual(type(rev.place_id), str)
        self.assertEqual(type(rev.user_id), str)
        self.assertEqual(type(rev.text), str)

    def test_instance(self):
        """ Test if is instance """
        rev = Review()
        self.assertIsInstance(rev, Review)

    def test_docstring(self):
        """ Test documentation """
        self.assertIsNotNone(Review.__doc__)


if __name__ == '__main__':
    unittest.main()
