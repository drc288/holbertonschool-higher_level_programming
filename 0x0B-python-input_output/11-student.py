#!/usr/bin/python3
""" Class Student - define class
"""


class Student:
    """ __init__ - init fname, lname and age """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ to_json - Convert to json """
        return self.__dict__
