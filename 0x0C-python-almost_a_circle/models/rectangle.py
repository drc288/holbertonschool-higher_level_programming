#!/usr/bin/python3
from models.base import Base
"""
Rectangle - create a object with contain the width and the height
in a rectangle and create two method
"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Init the constructor - Private
        instance attributes change
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
        """
        __str__ - return the rectangle class str
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def area(self):
        """
        area - return the area of height and width
        """
        a = self.height * self.width
        return a

    def display(self):
        """
        display - get the display for height and width
        """
        space = self.x
        n_line = self.y
        if n_line != 0:
            for i in range(n_line):
                print()
        for i in range(self.height):
            if space != 0:
                print(" " * space, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """
        update - update the Rectangle, 
        """
        # Get the len of args
        len_args = len(args)
        len_kwargs = len(kwargs)
        if len_kwargs != 0 and len_args == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "height":
                    self.height = value
                if key == "width":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        if len_args != 0:
            for i, data in enumerate(args):
                if i == 0:
                    self.id = data
                if i == 1:
                    self.width = data
                if i == 2:
                    self.height = data
                if i == 3:
                    self.x = data
                if i == 4:
                    self.y = data

    @property
    def width(self):
        """
        Width - Getter for Width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width - Setter for Width, validate the data
        """
        if isinstance(value, str):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Height - getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height - Setter for Height, validate the data"""
        if isinstance(value, str):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x - setter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ x - Setter for x, validate the data """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        y - setter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ y - Setter for y, validate the data"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
