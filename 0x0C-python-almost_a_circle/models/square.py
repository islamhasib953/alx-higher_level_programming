#!/usr/bin/python3
""" Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns the string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
