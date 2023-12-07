#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = 0
    my_set = set(my_list)
    for i in my_set:
        x += i
    return x
