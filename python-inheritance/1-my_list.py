#!/usr/bin/python3
"""Module that defines a MyList class that inherits from list"""


class MyList(list):
    """Class that inherits from list with print_sorted method"""

    def print_sorted(self):
        """Print the list in ascending sorted order"""
        print(sorted(self))
