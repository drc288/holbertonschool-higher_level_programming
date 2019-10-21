#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
""" TestArea - To prube the class base
"""


class TestArea(unittest.TestCase):
    """
    test_area - test cases for area
    """
    def test_area(self):
        print("Test area")
        """ INIT VARIABLES """
        ins_1 = Rectangle(10, 5)
        ins_2 = Rectangle(10, 4, 0, 0, 10)
        ins_3
        """ TEST """
        self.assertEqual(ins_1.area(), 50)
        self.assertEqual(ins_2.area(), 40)
    """
    test_errors - test cases in error
    """
    def test_errors(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "A")
            Rectangle("A", 10)