#!/usr/bin/python3
"""This module contains unit tests for the Rectangle class."""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Unit tests for Rectangle class."""

    def setUp(self):
        """Resets __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_instance(self):
        """Tests Rectangle instance creation."""
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Rectangle)

    def test_id_auto(self):
        """Tests auto-assigned id."""
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 1)

    def test_id_given(self):
        """Tests given id."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_width(self):
        """Tests width attribute."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)

    def test_height(self):
        """Tests height attribute."""
        r = Rectangle(10, 2)
        self.assertEqual(r.height, 2)

    def test_x(self):
        """Tests x attribute."""
        r = Rectangle(10, 2, 3)
        self.assertEqual(r.x, 3)

    def test_y(self):
        """Tests y attribute."""
        r = Rectangle(10, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_width_type_error(self):
        """Tests TypeError for width."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_height_type_error(self):
        """Tests TypeError for height."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_x_type_error(self):
        """Tests TypeError for x."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "3")

    def test_y_type_error(self):
        """Tests TypeError for y."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, "4")

    def test_width_value_error(self):
        """Tests ValueError for width."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_height_value_error(self):
        """Tests ValueError for height."""
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_x_value_error(self):
        """Tests ValueError for x."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3)

    def test_y_value_error(self):
        """Tests ValueError for y."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -4)

    def test_area(self):
        """Tests area method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Tests __str__ method."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Tests update method with args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Tests update method with kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1, width=2)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.width, 2)

    def test_to_dictionary(self):
        """Tests to_dictionary method."""
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertEqual(type(d), dict)
        self.assertIn('id', d)
        self.assertIn('width', d)
        self.assertIn('height', d)
        self.assertIn('x', d)
        self.assertIn('y', d)


if __name__ == "__main__":
    unittest.main()
