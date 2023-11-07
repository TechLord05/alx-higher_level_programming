#!/usr/bin/python3
""" class MyInt that inherits from int """


class MyInt(int):
    """ class MyInt that inherits from int """

    def __eq__(self, other):
        """Override the equality operator (==)"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator (!=)"""
        return super().__eq__(other)
