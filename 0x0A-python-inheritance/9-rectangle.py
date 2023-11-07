#!/usr/bin/python3
""" class BaseGeometry """


class BaseGeometry:
    """ class BaseGeometry """

    def area(self):
        """ Calculate and returns the rectangle area """

    def integer_validator(self, name, value):
        """
        integer_validator method that validates value
        raises
        TypeError  : <name> must be an integer
        ValueError : <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
        Rectangle.integer_validator(self, "width", width)
        self.__width = width
        Rectangle.integer_validator(self, "height", height)
        self.__height = height

    def area(self):
        """ calculate the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ return a rectangle description: [Rectangle] <width>/<height> """
        return f"[Rectangle] {self.__width}/{self.__height}"
