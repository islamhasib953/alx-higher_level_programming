#!/usr/bin/python3

"""5-save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file"""
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
