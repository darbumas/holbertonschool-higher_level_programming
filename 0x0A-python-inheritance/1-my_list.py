#!/usr/bin/python3
"""Module defines a class ``MyList`` that inherits from the class ``list``."""


class MyList(list):
    """Class derived from supper class ``list``."""
    def print_sorted(self):
        """Prints a sorted (ascending order) list."""
        print(sorted(self))
