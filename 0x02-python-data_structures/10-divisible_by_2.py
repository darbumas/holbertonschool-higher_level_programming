#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_list1 = []
    for num in my_list:
        my_list1.append(num % 2 == 0)
    return my_list1

