#!/usr/bin/python3
""" BaseGeometry - create a empty object BaseGeometry
"""
class BaseGeometry:
    """ area - get the area (error Exeption)
    """
    def area(self):
        raise Exception("area() is not implemented")
    """ integer_validator - validate if value is not int or if <= to 0
    """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(str(name)))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(str(name)))

""" Rectangle - unherits BaseGeometry
"""
class Rectangle(BaseGeometry):
    """ __init__ - initializate the width and height
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height" ,height)
        self.__height = height
    """ __str__ - return a example code of rectangle
    """
    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
    """ area - implement area in Rectangle
    """
    def area(self):
        return self.__width * self.__height

""" Square - create the squere area and str
"""
class Square(Rectangle):
    """ __init__ - init the program
    """
    def __init__(self, size):
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size
    """ __str__ - return a example code of Square
    """
    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)