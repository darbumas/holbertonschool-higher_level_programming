#!/usr/bin/python3
"""Module creates a class ``Rectangle`` derived fom parent
class ``Base``."""

from models.base import Base


class Rectangle(Base):
    """class inherits from parent -> ``Base``."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """public getter method for width"""
        return self.__width

    @width.setter
    def width(self, val):
        """public setter method for width"""
        self.__width = val

    @property
    def height(self):
        """public getter method for height"""
        return self.__width

    @height.setter
    def height(self, val):
        """public setter method for height"""
        self.__height = val

    @property
    def x(self):
        """public getter method for x"""
        return self.__x

    @x.setter
    def x(self, val):
        """public setter method for x"""
        self.__x = val

    @property
    def y(self):
        """public getter method for y"""
        return self.__y

    @y.setter
    def y(self, val):
        """public setter methode for y"""
        self.__y = val
