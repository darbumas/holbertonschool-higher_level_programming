#!/usr/bin/python3
"""Module defines a ƒ() ``inherits_from(obj, a_class)`` that evaluates and
returns True if 'obj' is an instance of a class that inherited (directly or
indirectly) from the specified class, otherwise False."""


from re import A


def inherits_from(obj, a_class):
    """Returns True if 'obj' is a subclass (directly or indirectly) of
    'a_class'."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
