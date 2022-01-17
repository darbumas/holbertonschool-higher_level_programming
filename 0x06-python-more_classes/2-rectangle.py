#!/usr/bin/python3
"""Module creates a class ``Rectangle``"""


class Rectangle:
    """This class has private instances width and height which
    have to be integers or TypeError exception message"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        """Defines how the object should be printed"""
        rectangle = ""
        if self.__width > 0 and self.__height > 0:
            for h in range(self.__height):
                for w in range(self.__width):
                    rectangle += "#"
                if h < self.__height - 1:
                    rectangle += "\n"
        return rectangle

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2
