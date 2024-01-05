#!/usr/bin/python3

"""Define Rectangle"""


class Rectangle:
    """Define Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size.

        Args:
            size (int): size. Defaults to 0.
        """
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """Instantition of onjecct.
        Args:
        __width(int): width of rectangle, default to zero
        __height(int): height of rectangle, default to zero
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        compute the area of rectangle
        Returns:
        area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """print the rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for x in range(self.__height):
            row = str(self.print_symbol) * self.__width
            rect.append(row)
        return "\n".join(rect)

    def __repr__(self):
        """epresentation of the rectangle using repr"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
