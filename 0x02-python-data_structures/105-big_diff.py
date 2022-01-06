#!/usr/bin/python3
def big_diff(my_list=[]):
    if len(my_list) <= 1:
        return 0
    big_diff = max(my_list) - min(my_list)
    return big_diff
