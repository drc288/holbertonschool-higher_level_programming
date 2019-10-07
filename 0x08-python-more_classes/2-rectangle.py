#!/usr/bin/python3
"""
    Rectangle - create a object with contain the width and the height
    in a rectangle and create two method
    area()
    perimeter()
    >>> r = Rectangle(2, 3)
"""


class Rectangle:
    """
    Rectangle: create width=0, height=0
    """

    """ Init the class """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """ Method """
    def area(self):
        a = int(self.height * self.width)
        return (a)

    def perimeter(self):
        if int(self.height) == 0 or int(self.width) == 0:
            p = 0
        else:
            p = int(2 * (self.height + self.width))
        return (p)

    """ For width """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """ For height """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
