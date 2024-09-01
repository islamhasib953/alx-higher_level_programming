#!/usr/bin/python3

"""9-student"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary"""
        return self.__dict__
