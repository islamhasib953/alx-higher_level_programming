#!/usr/bin/python3
def max_integer(my_list=[]):
    x = my_list[0]
    for i in range(len(my_list)):
        if x < my_list[i]:
            x = my_list[i]
    return x


my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
