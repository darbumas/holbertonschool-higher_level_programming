#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, val in a_dictionary.items():
        if val == value:
            del a_dictionary[key]
            return complex_delete(a_dictionary, value)
    return a_dictionary
