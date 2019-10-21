#!/usr/bin/python3
from models.base import Base
"""
Rectangle - create a object with contain the width and the height
in a rectangle and create two method
"""


class Rectangle(Base):
    """
    Init the constructor
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Private instance attributes change
        the variables to public and return in
        setter and getter the private value
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        """ Call the super class with id """
        super().__init__(id)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)
    """
    area - return the area of height and width
    """
    def area(self):
        a = self.height * self.width
        return a
    """
    display - get the display for height and width
    """
    def display(self):
        for i in range(self.height):
            print("#" * self.width)

    """
    Width - setter and getter
    for Width, validate the data
    """
    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter """
        if isinstance(value, str):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """
    Height - setter and getter
    for Height, validate the data
    """
    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter """
        if isinstance(value, str):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """
    x - setter and getter
    for x, validate the data
    """
    @property
    def x(self):
        """ Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    """
    y - setter and getter
    for y, validate the data
    """
    @property
    def y(self):
        """ Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
