#!/usr/bin/python3

"""Define Rectangle"""


class Rectangle:
    """Define Rectangle"""

    def __init__(self, width=0, height=0):
        """Instantition of onjecct.
        Args:
        __width(int): width of rectangle, default to zero
        __height(int): height of rectangle, default to zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter width
        Returns:
        int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter height

        Returns:
        int: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
