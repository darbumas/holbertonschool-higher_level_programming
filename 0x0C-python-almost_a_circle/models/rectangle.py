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
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """public getter method for height"""
        return self.__width

    @height.setter
    def height(self, val):
        """public setter method for height"""
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """public getter method for x"""
        return self.__x

    @x.setter
    def x(self, val):
        """public setter method for x"""
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """public getter method for y"""
        return self.__y

    @y.setter
    def y(self, val):
        """public setter methode for y"""
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """public method returns the area of the ``Rectangle`` instance"""
        return self.__width * self.__height

    def display(self):
        """public method that prints to stdout the ``Rectangle instance``
        with "#" characters."""
        for y in range(self.__height):
            for x in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overides the builtin "__str__" method for a nicer representation
        of the ``Rectangle`` instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)
