#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        x, y = 0, 0
        for i in range(len(my_list)):
            x += my_list[i][0] * my_list[i][1]
            y += my_list[i][1]
    return x / y
