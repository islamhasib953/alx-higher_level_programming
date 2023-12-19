#!/usr/bin/python3
"""
creates a square class object
"""


class Square:
    """
    square class
    """
    def __init__(self, size=0):
        """
        constractor for square class
        Args:
        size (int) : size of sauare, defualts to zero
        """
        self.__size = size
    @property
    def size(self):
        """size getter"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("ize must be >= 0")
        self.__size = value

    def area(self):
        """
        returns the current square area
        """
        return self.__size * self.__size
