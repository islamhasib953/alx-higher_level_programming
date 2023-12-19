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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("ize must be >= 0")
        self.__size = size
