#!/usr/bin/python3
"""Module that defines a BaseGeometry class with area method"""


class BaseGeometry:
    """Class that defines a base geometry with area method"""

    def area(self):
        """Raise an Exception since area is not implemented

        Raises:
            Exception: always raises area() is not implemented
        """
        raise Exception("area() is not implemented")
