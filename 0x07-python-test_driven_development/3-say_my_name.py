#!/usr/bin/python3
"""
    say_my_name - say my name
    usage: My name is <first name> <last name>
    >>> ay_my_name(first_name, last_name="")
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name - say the name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
