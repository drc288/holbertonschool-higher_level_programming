#!/usr/bin/python3
""" Class Student - define class
"""


class Student:
    """ __init__ - init fname, lname and age """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to_json - Convert to json """
        if attrs is None:
            return self.__dict__
        tmp_dict = dict()
        for key in attrs:
            if key in self.__dict__.keys():
                tmp_dict[key] = self.__dict__[key]
        return tmp_dict
        