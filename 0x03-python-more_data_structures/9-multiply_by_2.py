#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dict = {}
    for val in a_dictionary.copy():
        my_dict[val] = a_dictionary.get(val) * 2
    return my_dict
