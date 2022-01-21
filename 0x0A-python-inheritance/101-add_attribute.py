#!/usr/bin/python3
"""Module defines a ƒ() ``add_attribute`` that adds a new attribute
 to an object if it's possible"""


def add_attribute(self, attr, value):
    """ƒ() add attribute to an object if possible, otherwise
    raises TypeError exception with a custom message"""
    if hasattr(self, '__dict__'):
        setattr(self, attr, value)
    else:
        raise TypeError("can't add new attribute")
