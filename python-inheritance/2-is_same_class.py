#!/usr/bin/python3
"""Module that defines is_same_class function"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class

    Args:
        obj: any object
        a_class: class to check against

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise
    """
    return type(obj) is a_class
