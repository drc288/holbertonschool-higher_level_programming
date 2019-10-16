#!/usr/bin/python3
""" inherits_from - identify if ibj are subclass of a_class
"""


def inherits_from(obj, a_class):
    """ issubclass - verify if subclass """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
