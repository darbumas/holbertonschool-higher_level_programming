#!/usr/bin/python3
"""Module defines a ƒ() ``is_kind_of_class(obj, a_class)`` that evaluates
inheritance. Returns True if object is an instance of a class
(or specified class), otherwise False."""


def is_kind_of_class(obj, a_class):
    """Returns True if 'obj' is an instance of 'a_class'"""
    return isinstance(obj, a_class)
