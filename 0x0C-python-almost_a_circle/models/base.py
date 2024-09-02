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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation"""
        name = cls.__name__ + ".json"
        all_lists = []
        if list_objs is not None:
            for obj in list_objs:
                all_lists.append(obj.to_dictionary())
        with open(name, "w") as f:
            f.write(cls.to_json_string(all_lists))

    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """create method"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)