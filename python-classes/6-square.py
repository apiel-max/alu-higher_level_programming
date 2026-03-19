#!/usr/bin/python3
"""Module that defines a Square class with size and position"""


class Square:
    """Class that defines a square by its size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance

        Args:
            size (int): size of the square, defaults to 0
            position (tuple): position of the square, defaults to (0, 0)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square

        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value (int): size of the square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square

        Returns:
            tuple: position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square

        Args:
            value (tuple): position of the square

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square

        Returns:
            int: area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters to stdout"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
