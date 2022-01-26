#!/usr/bin/python3
"""Module creates a class ``Square`` derived from parent
class ``Rectangle``."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """new class inherits from parent -> ``Rectangle``."""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overides the builtin "__str__" method for a nicer representation
        of the ``Square`` instance"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x,
                                             self.y, self.height)
