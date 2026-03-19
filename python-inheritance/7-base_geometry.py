#!/usr/bin/python3
"""Module that defines a BaseGeometry class with integer_validator"""


class BaseGeometry:
    """Class that defines a base geometry with validation"""

    def area(self):
        """Raise an Exception since area is not implemented

        Raises:
            Exception: always raises area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value is a positive integer

        Args:
            name (str): name of the parameter
            value (int): value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
