#!/usr/bin/python3
"""
    print_square - print squere of ´#´
    >>> print_square(1)
    #
"""


def print_square(size):
    """
        print_square - print square to size * size
    """
    square = "#"
    if type(size) is int:
        if type(size) is float and size < 0:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        for i in range(size):
            for j in range(size):
                print(square, end="")
            print()
    else:
        raise TypeError("size must be an integer")
