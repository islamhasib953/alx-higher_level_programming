#!/usr/bin/python3
"""9-rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return the area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of a Rectangle object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
