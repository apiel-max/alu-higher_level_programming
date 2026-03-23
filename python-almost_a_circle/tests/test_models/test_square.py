#!/usr/bin/python3
"""This module contains unit tests for the Square class."""
import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Unit tests for Square class."""

    def setUp(self):
        """Resets __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_instance(self):
        """Tests Square instance creation."""
        s = Square(5)
        self.assertIsInstance(s, Square)

    def test_id_auto(self):
        """Tests auto-assigned id."""
        s = Square(5)
        self.assertEqual(s.id, 1)

    def test_size(self):
        """Tests size attribute."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_x(self):
        """Tests x attribute."""
        s = Square(5, 2)
        self.assertEqual(s.x, 2)

    def test_y(self):
        """Tests y attribute."""
        s = Square(5, 2, 3)
        self.assertEqual(s.y, 3)

    def test_size_type_error(self):
        """Tests TypeError for size."""
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_value_error(self):
        """Tests ValueError for size."""
        with self.assertRaises(ValueError):
            Square(-5)

    def test_area(self):
        """Tests area method."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        """Tests __str__ method."""
        s = Square(5, 2, 3, 1)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 5")

    def test_size_setter(self):
        """Tests size setter."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_update_args(self):
        """Tests update method with args."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Tests update method with kwargs."""
        s = Square(5)
        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)

    def test_to_dictionary(self):
        """Tests to_dictionary method."""
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertEqual(type(d), dict)
        self.assertIn('id', d)
        self.assertIn('size', d)
        self.assertIn('x', d)
        self.assertIn('y', d)


if __name__ == "__main__":
    unittest.main()
