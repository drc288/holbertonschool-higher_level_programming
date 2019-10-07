#!/usr/bin/python3
"""
    Rectangle - create a object with contain the width and the height
    in a rectangle and create two method
    area()
    perimeter()
    str message
    repr message
    Del
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

    """ __str__ & __repr__ Method """
    def __str__(self):
        str_n = ""
        if self.height == 0 or self.width == 0:
            return str_n
        for i in range(self.height):
            for j in range(self.width):
                str_n += "#"
            if i == self.height - 1:
                break
            str_n += "\n"
        return str_n

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    """ Delete """
    def __del__(self):
        print("Bye rectangle...")

    """ Public method """
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
