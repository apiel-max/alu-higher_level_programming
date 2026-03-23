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

    def test_width_zero(self):
        """Tests ValueError for width = 0."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_zero(self):
        """Tests ValueError for height = 0."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_display_no_x_y(self):
        """Tests display without x and y."""
        r = Rectangle(2, 2)
        from io import StringIO
        import sys
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_no_y(self):
        """Tests display without y."""
        r = Rectangle(2, 2, 1)
        from io import StringIO
        import sys
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), " ##\n ##\n")

    def test_display_with_x_y(self):
        """Tests display with x and y."""
        r = Rectangle(2, 2, 1, 1)
        from io import StringIO
        import sys
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")

    def test_create_id(self):
        """Tests create with id only."""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        """Tests create with id and width."""
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_create_id_width_height(self):
        """Tests create with id, width and height."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_create_id_width_height_x(self):
        """Tests create with id, width, height and x."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_create_all(self):
        """Tests create with all attributes."""
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_save_to_file_None(self):
        """Tests save_to_file with None."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Tests save_to_file with empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file(self):
        """Tests save_to_file with one Rectangle."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            self.assertIn('width', f.read())

    def test_load_from_file_no_file(self):
        """Tests load_from_file when file doesn't exist."""
        import os
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        """Tests load_from_file when file exists."""
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Rectangle)


if __name__ == "__main__":
    unittest.main()
