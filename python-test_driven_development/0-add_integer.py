#!/usr/bin/python3
"""This module provides a function that adds two integers.

The function handles integers and floats, casting floats to integers
before addition, and raises TypeError for invalid input types.
"""


def add_integer(a, b=98):
    """Adds two integers or floats and returns an integer result.

    Raises TypeError if a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
