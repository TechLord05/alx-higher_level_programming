#!/usr/bin/python3
""" class BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry

""" A class representing a Rectangle  that inherits from BaseGeometry """


class Rectangle(BaseGeometry):
    """
    This class allows you to create and manipulate Rectangle objects.
    Each Rectangle is defined by its width and height
    """
    def __init__(self, width, height):
        """Initialize a new Rectangle.
            Args:
                width (int): The width of the new Rectangle.
                height (int): The height of the new Rectangle.
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
