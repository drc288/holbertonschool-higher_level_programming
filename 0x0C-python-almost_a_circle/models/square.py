#!/usr/bin/python3
"""
Square - create a object square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Init the constructor - super().__init__(size, size, x, y)
        call the super class
        """
        super().__init__(size, size, x, y)

    def __str__(self):
        """
        __str__ - return the rectangle class str
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)

    def to_dictionary(self):
        """
        to_dictionary - create dictionary for square
        """
        return {'id': self.id, 'y': self.y, 'x': self.x, 'size': self.size}

    def update(self, *args, **kwargs):
        """
        update - update the Rectangle
        """
        # Get the len of args
        len_args = len(args)
        len_kwargs = len(kwargs)
        if len_kwargs != 0 and len_args == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        if len_args != 0:
            for i, data in enumerate(args):
                if i == 0:
                    self.id = data
                if i == 1:
                    self.size = data
                if i == 2:
                    self.x = data
                if i == 3:
                    self.y = data

    @property
    def size(self):
        """
        size - method getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size - method setter
        """
        self.width = value
        self.height = value
