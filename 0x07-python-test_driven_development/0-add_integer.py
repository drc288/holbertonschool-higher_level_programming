#!/usr/bin/python3
"""
    add_integer - add a to b
    >>> add_integer(5, 5)
    10
"""


def add_integer(a, b=98):
    """
    add_integer - add two numbers
    """
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    elif type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
