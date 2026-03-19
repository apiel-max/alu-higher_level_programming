#!/usr/bin/python3
"""Module that defines a Rectangle class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that defines a rectangle by its width and height"""

    def __init__(self, width, height):
        """Initialize a new Rectangle instance

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle

        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Return string description of the rectangle

        Returns:
            str: rectangle description in format [Rectangle] width/height
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
