#!/usr/bin/python3
""" is_same_class - detect if the obj is the same of a_class
    >>> a = 1
    >>> is_same_class(a, int)
    True
"""
def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
        return False
