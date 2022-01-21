#!/usr/bin/python3
"""Module creates a class ``MyInt`` derived from parent class ``int``."""


class MyInt(int):
    """Class inherits from parent class ``int``."""
    pass

    def __eq__(self, other):
        """Custom implementation of the 'Python' native ƒ(),
        in this case to invert it"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Custom implementation of the 'Python' native ƒ(),
        to invert it."""
        return int(self) == int(other)
