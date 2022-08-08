#!/usr/bin/python3
""" Unit tests for Amenity class """

import unittest
from models.amenity import Amenity
import pep8


class Test_Amenity(unittest.TestCase):
    """Base class tests"""

    def test_pep8_conformance_amenity(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_hasattr(self):
        """ Test if an object has an attribute """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))

    def test_type_amenity(self):
        """ Test the type of the attribute """
        amenity = Amenity()
        self.assertEqual(type(amenity.name), str)

    def test_instance(self):
        """ Test if is instance """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_docstring(self):
        """ Test documentation """
        self.assertIsNotNone(Amenity.__doc__)


if __name__ == '__main__':
    unittest.main()
