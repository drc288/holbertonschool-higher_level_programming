#!/usr/bin/python3
""" BaseGeometry - create a empty object BaseGeometry
"""
class BaseGeometry:
    """ area - get the area (error Exeption)
    """
    def area(self):
        raise Exception("area() is not implemented")
    """ integer_validator - validate if value is not int or if <= to 0
    """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(str(name)))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(str(name)))