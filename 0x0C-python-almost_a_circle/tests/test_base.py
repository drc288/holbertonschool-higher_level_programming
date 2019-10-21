#!/usr/bin/python3
import unittest
from models.base import Base
""" TestBase - To prube the class base
"""


class TestBase(unittest.TestCase):
    """
    test_id - test case for id
    """
    def test_id(self):
        print("Test id")
        """ INIT VARIABLES """
        inst_1 = Base()
        inst_2 = Base()
        inst_3 = Base(13)
        inst_4 = Base(-1)
        inst_5 = Base()
        inst_6 = Base("a")
        inst_7 = Base({id: 1})
        inst_8 = Base(float('NaN'))
        inst_9 = Base([8])
        inst_10 = Base(3.14)
        inst_11 = Base((6, 9))
        inst_12 = Base({4, 2, 0})
        """ TEST """
        self.assertEqual(inst_1.id, 1)
        self.assertEqual(inst_2.id, 2)
        self.assertEqual(inst_3.id, 13)
        self.assertEqual(inst_4.id, -1)
        self.assertEqual(inst_5.id, 3)
        self.assertEqual(inst_6.id, "a")
        self.assertEqual(inst_7.id, {id: 1})
        self.assertNotEqual(inst_8.id, inst_8.id)
        self.assertEqual(inst_9.id,[8])
        self.assertEqual(inst_10.id, 3.14)
        self.assertEqual(inst_11.id, (6, 9))
        self.assertEqual(inst_12.id, {0, 2, 4})

    """
    test_issubclass - Verify is the class
    """
    def test_issubclass(self):
        inst_1 = Base()
        """ TEST """
        self.assertIsInstance(inst_1, Base)
        self.assertIsNot(inst_1, Base)
