#!/usr/bin/python3
"""Module creates a class with a public intance method."""


class BaseGeometry:
    """Class with a public instance method that doesn't do anything."""
    def area(self):
        """Public method raises exception message"""
        raise Exception("area() is not implemented")
