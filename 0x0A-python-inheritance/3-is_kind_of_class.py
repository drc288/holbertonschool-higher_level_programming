#!/usr/bin/python3
""" is_kind_class - look if the obj is the a_class and if is a object
    >>> a = 1
    >>> is_kind_of_class(a , int)
    True
    >>> is_kind_of_class(a , obj)
    True
"""
def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)
