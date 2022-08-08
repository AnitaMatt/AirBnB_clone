#!/usr/bin/python3
"""Test base model"""

import unittest
from models.base_model import BaseModel
import pep8


class Test_Base(unittest.TestCase):
    """Base class tests"""

    model = BaseModel()

    def test_validate(self):
        """ validate attributes """
        self.model.name = "Holberton"
        self.model.my_number = 89
        self.model.save()

    def test_existing_class(self):
        """ test if the class exist """
        self.assertEqual(str(type(self.model)),
                         "<class 'models.base_model.BaseModel'>")

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
