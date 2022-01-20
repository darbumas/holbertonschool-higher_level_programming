#!/usr/bin/python3
"""Module defines a ƒ() ``is_same_classe(obj, a_class)`` that evaluates if
an object (passed as first arg) is an instance of a class (2nd arg)."""


def is_same_class(obj, a_class):
    """Returns True if 'obj' is an instance of 'a_class`; otherwise False."""
    return type(obj) == a_class
