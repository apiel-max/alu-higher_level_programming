#!/usr/bin/python3
"""Module that defines a lookup function"""


def lookup(obj):
    """Return list of available attributes and methods of an object

    Args:
        obj: any object

    Returns:
        list: list of available attributes and methods
    """
    return dir(obj)
