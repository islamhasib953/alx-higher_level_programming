#!/usr/bin/python3
"""8-rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        super().__init__()
        self.width = width
        self.height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
