#!/usr/bin/python3
""" Unit tests for Place class """

import unittest
from models.place import Place
import pep8


class Test_Amenity(unittest.TestCase):
    """Base class tests"""

    def test_pep8_conformance_place(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_hasattr(self):
        """ Test if an object has an attribute """
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_type_place(self):
        """ Test the type of the attribute """
        place = Place()
        self.assertEqual(type(place.city_id), str)
        self.assertEqual(type(place.user_id), str)
        self.assertEqual(type(place.name), str)
        self.assertEqual(type(place.description), str)
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(type(place.amenity_ids), list)

    def test_instance(self):
        """ Test if is instance """
        place = Place()
        self.assertIsInstance(place, Place)

    def test_docstring(self):
        """ Test documentation """
        self.assertIsNotNone(Place.__doc__)


if __name__ == '__main__':
    unittest.main()
