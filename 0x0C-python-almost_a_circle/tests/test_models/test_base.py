#!/usr/bin/python3
import unittest
from models.base import Base
""" TestBase - To prube the class base
"""


class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        in_1 = Base()
        self.assertEqual(in_1.id, 1)
        
    def test_two_instance(self):
        in_1 = Base()
        in_2 = Base()
        self.assertEqual(in_2.id, 2)
    
    def test_id_value(self):
        in_1 = Base(10)
        self.assertEqual(in_1.id, 10)
    
    def test_negative_number(self):
        in_1 = Base(-1)
        self.assertEqual(in_1.id, -1)
    
    def test_string(self):
        in_1 = Base("String")
        self.assertEqual(in_1.id, "String")

    def test_dict_base(self):
        in_1 = Base({id: 1})
        self.assertEqual(in_1.id, {id: 1})
    
    def test_float_base(self):
        in_1 = Base(float('NaN'))
        self.assertNotEqual(in_1.id, in_1.id)
    
    def test_list(self):
        in_1 = Base([420])
        self.assertEqual(in_1.id, [420])

    def test_float2(self):
        in_1 = Base(3.14)
        self.assertEqual(in_1.id, 3.14)
        
    def test_tuple(self):
        in_1 = Base((6, 9))
        self.assertEqual(in_1.id, (6, 9))
    
    def test_array(self):
        in_1 = Base({4, 2, 0})
        self.assertEqual(in_1.id, {0, 2, 4})

if __name__ == '__main__':
    unittest.main()