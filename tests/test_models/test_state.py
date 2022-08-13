#!/usr/bin/python3
""" Unit tests for State class """

import unittest
from models.state import State
import pep8


class Test_State(unittest.TestCase):
    """Base class tests"""

    def test_pep8_conformance_state(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_hasattr(self):
        """ Test if an object has an attribute """
        st = State()
        self.assertTrue(hasattr(st, "name"))

    def test_type_state(self):
        """ Test the type of the attribute """
        st = State()
        self.assertEqual(type(st.name), str)

    def test_instance(self):
        """ Test if is instance """
        st = State()
        self.assertIsInstance(st, State)

    def test_docstring(self):
        """ Test documentation """
        self.assertIsNotNone(State.__doc__)


if __name__ == '__main__':
    unittest.main()
