#!/usr/bin/python3

"""6-base_geometry"""


class BaseGeometry:
    """Write an empty class BaseGeometry"""

    def area(self):
        """Public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
