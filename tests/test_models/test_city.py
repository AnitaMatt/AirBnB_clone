#!/usr/bin/python3
""" Unit tests for City class """

import unittest
from models.city import City
import pep8


class Test_City(unittest.TestCase):
    """Base class tests"""

    def test_pep8_conformance_city(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_hasattr(self):
        """ Test if an object has an attribute """
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))

    def test_type_city(self):
        """ Test the type of the attribute """
        city = City()
        self.assertEqual(type(city.name), str)
        self.assertEqual(type(city.state_id), str)

    def test_instance(self):
        """ Test if is instance """
        city = City()
        self.assertIsInstance(city, City)

    def test_docstring(self):
        """ Test documentation """
        self.assertIsNotNone(City.__doc__)


if __name__ == '__main__':
    unittest.main()
