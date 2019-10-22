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
        """
        
        """
        print("Test area")
        """ INIT VARIABLES """
        ins_1 = Rectangle(10, 5)
        ins_2 = Rectangle(10, 4, 0, 0, 10)
        ins_3 = Rectangle(2.0, 3.8)
        """ TEST """
        self.assertEqual(ins_1.area(), 50)
        self.assertEqual(ins_2.area(), 40)
        self.assertEqual(ins_3.area(), 7.6)
        del(ins_1)
        del(ins_2)
        del(ins_3)

    def test_errors(self):
        """
        test_errors - test cases in error
        """
        with self.assertRaises(TypeError):
            Rectangle(10, "A")
            Rectangle("A", 10)
            Rectangle()
            Rectangle(None,None)
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
            Rectnagle(1, -2)
    
    if __name__ == '__main__':
        unittest.main()