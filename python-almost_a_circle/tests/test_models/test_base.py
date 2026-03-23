#!/usr/bin/python3
"""This module contains unit tests for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit tests for Base class."""

    def setUp(self):
        """Resets __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto(self):
        """Tests auto-assigned id."""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_auto_increment(self):
        """Tests auto-incremented id."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_given(self):
        """Tests given id."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_mixed(self):
        """Tests mixed id assignment."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_to_json_string_empty(self):
        """Tests to_json_string with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Tests to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string(self):
        """Tests to_json_string with valid list."""
        d = [{'id': 1, 'width': 10}]
        self.assertEqual(type(Base.to_json_string(d)), str)

    def test_from_json_string_empty(self):
        """Tests from_json_string with empty string."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_none(self):
        """Tests from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string(self):
        """Tests from_json_string with valid string."""
        s = '[{"id": 1, "width": 10}]'
        self.assertEqual(type(Base.from_json_string(s)), list)


if __name__ == "__main__":
    unittest.main()
