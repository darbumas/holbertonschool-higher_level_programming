#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        weight_mult, weight_sum = 0, 0
        for num in my_list:
            weight_mult += (num[0] * num[1])
        for num in my_list:
            weight_sum += num[1]
        return weight_mult / weight_sum
    else:
        return 0
