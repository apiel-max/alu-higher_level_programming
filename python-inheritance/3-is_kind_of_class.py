#!/usr/bin/python3
"""Module that defines is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclass

    Args:
        obj: any object
        a_class: class to check against

    Returns:
        bool: True if obj is an instance of a_class or inherited class
    """
    return isinstance(obj, a_class)
