#!/usr/bin/python3
"""Module creates a new class ``Rectangle`` derived from parent
class ``BaseGeometry``."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class inherits from parent class 'BaseGeometry"""
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
