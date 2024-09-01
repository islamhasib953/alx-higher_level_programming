#!/usr/bin/python3

"""10-student"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, list_items=None):
        """retrieves a dictionary"""
        if list_items is None:
            return self.__dict__
        else:
            return {
                key: value for key, value in self.__dict__.items() if key in list_items
            }
