#!/usr/bin/python3
""" base """
import json


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
