#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    x = 0
    for i in a_dictionary:
        if i == key:
            a_dictionary[key] = value
            x = 1
    if x == 0:
        a_dictionary[key] = value
    return a_dictionary
