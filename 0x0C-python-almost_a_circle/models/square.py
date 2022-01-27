#!/usr/bin/python3
"""Module creates a class ``Square`` derived from parent
class ``Rectangle``."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """new class inherits from parent -> ``Rectangle``."""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """overides the builtin "__str__" method for a nicer representation
        of the ``Square`` instance"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x,
                                             self.y, self.__height)

    @property
    def size(self):
        """public getter method for size"""
        return self.__width

    @size.setter
    def size(self, val):
        """public setter method for size"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val
        self.__height = val

    def update(self, *args, **kwargs):
        """public method to update instance attributes"""
        if args is None or len(args) == 0:
            for attr in kwargs:
                if hasattr(self, attr):
                    setattr(self, attr, kwargs[attr])
        attrs = ['id', 'size', 'x', 'y']
        for i in range(len(args)):
            setattr(self, attrs[i], args[i])

    def to_dictionary(self):
        """public method returns the dictionary representation of a
        square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
