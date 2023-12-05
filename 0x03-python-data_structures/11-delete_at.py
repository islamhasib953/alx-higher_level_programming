#!/usr/bin/python3
def delet(my_list=[], idx=0):
    if idx < len(my_list):
        my_list.pop(idx)
    return my_list


def delete_at(my_list=[], idx=0):
    return delet(my_list, idx)
