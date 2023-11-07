#!/usr/bin/python3
""" import class Rectangle """

Rectangle = __import__('9-rectangle').Rectangle

""" class Square """


class Square(Rectangle):
    """
    This class allows you to create and manipulate Square objects.
    Each Square is defined by your size
    """
    def __init__(self, size):
        """Initialize a new Square.
            Args:
                size (int): The size of the new Square.
        """
        Square.integer_validator(self, "size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ return a squre description: [Square] <width>/<height> """
        return f"[Square] {self.__size}/{self.__size}"
