#!/usr/bin/python3
"""Module that defines a Square class that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a square by its size"""

    def __init__(self, size):
        """Initialize a new Square instance

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
