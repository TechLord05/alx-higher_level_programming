#!/usr/bin/python3
"""Module with a class"""


class Rectangle:
    """Class that represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
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
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            result = 0
        else:
            result = (2 * self.__width) + (2 * self.__height)
        return result
