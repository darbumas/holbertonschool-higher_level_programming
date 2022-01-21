#!/usr/bin/python3
"""Module defines a ƒ() to read from a file and prints it to stdout."""


def read_file(filename=""):
    """Reads from a file and prints content to stdout."""
    with open(filename, mode="r", encoding="utf-8") as MyFile:
        print(MyFile.read(), end="")
