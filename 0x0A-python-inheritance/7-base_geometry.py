#!/usr/bin/python3
"""Module creates a class with two public intance methods."""


class BaseGeometry:
    """Class with a public instance method that doesn't do anything."""
    def area(self):
        """Public method raises exception message"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Public method validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
