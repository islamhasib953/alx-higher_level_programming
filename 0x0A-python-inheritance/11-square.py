#!/usr/bin/python3

"""11-square"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with size"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return area"""
        return self.__size**2

    def __str__(self):
        """Square a string representation of a Square object"""
        return "[Square] {}/{}".format(self.__size, self.__size)
