#!/usr/bin/python3
""" Module defines a function ``say_my_name()`` with two parameter arguments.
Both arguments must be of type string.
The second argument is given a default value of an empty string; which means
that in calling the function, there must be at least one argument provided.
"""


def say_my_name(first_name, last_name=""):
    """ prints the value of ``first_name`` and ``last_name`` if and only if
    they are strings. Second argument is optional
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
