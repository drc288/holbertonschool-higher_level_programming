#!/usr/bin/python3
""" Class Base
"""


class Base:
    """ private class attribute """
    __nb_objects = 0
    """ Init the constructor
    """
    def __init__(self, id=None):
        """ Asign data to id """
        if id is not None:
            self.id = id
        else:
            """ Accessing the private attribute and assigning it a new value
            """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
