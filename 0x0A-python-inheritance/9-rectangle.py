#!/usr/bin/python3
"""Module creates a new class ``Rectangle`` derived from parent
class ``BaseGeometry``."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class inherits from parent class 'BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Public instance method, calculates area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Nice string representation of string"""
        return "[Rectangle] %d/%d" % (self.__width, self.__height)
