#!/usr/bin/python3
"""Module creates a class ``Rectangle`` derived fom parent
class ``Base``."""

from models.base import Base


class Rectangle(Base):
    """class inherits from parent -> ``Base``."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

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
        return self.__height

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
        print("\n" * self.__y, end="")
        for y in range(self.__height):
            print(" " * self.__x, end="")
            for x in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overides the builtin "__str__" method for a nicer representation
        of the ``Rectangle`` instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """public method assigns argument to each instance attribute"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        arg_idx = 0
        """if args is not empty, skip kwargs"""
        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, attrs[arg_idx], args[arg_idx])
                arg_idx += 1

        for key, value in kwargs.items():
            for i in range(len(attrs)):
                if key == attrs[i]:
                    setattr(self, attrs[i], value)

    def to_dictionary(self):
        """public method returns the dictionary representation of a
        rectangle instance."""
        return{"id": self.id, "width": self.__width, "height": self.__height,
               "x": self.__x, "y": self.__y}
