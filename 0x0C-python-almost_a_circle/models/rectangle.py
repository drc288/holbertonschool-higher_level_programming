#!/usr/bin/python3
from models.base import Base
"""
Rectangle - class inherits from Base
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
        """ Setter """
        return self.__x
    @x.setter
    def x(self, value):
        """ Getter """
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
        """ Setter """
        return self.__y  
    @y.setter
    def y(self, value):
        """ Getter """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
    