#!/usr/bin/python3
""" Unit tests for User class """

import unittest
from models.user import User
import pep8


class Test_User(unittest.TestCase):
    """Base class tests"""

    def test_pep8_conformance_user(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_hasattr(self):
        """Test if an object has an attribute"""
        user = User()
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(hasattr(user, "__init__"))

    def test_type_user(self):
        """ Test the type of the attribute """
        user = User()
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.password), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)

    def test_instance(self):
        """ Test if is instance """
        user = User()
        self.assertIsInstance(user, User)

    def test_docstring(self):
        """ Test documentation """
        self.assertIsNotNone(User.__doc__)


if __name__ == '__main__':
    unittest.main()
