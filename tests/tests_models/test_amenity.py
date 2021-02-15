#!/usr/bin/python3
""" Unit tests Amenity class """
from models.amenity import Amenity
import unittest
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """ Unit tests Amenity class """

    def setUp(self):
        self.am_1 = Amenity()
        self.am_1.name = "Kitchen"
        self.am_2 = Amenity()

    def test_attr_base(self):
        self.assertIsNotNone(self.am_1.id)
        self.assertIsNotNone(self.am_1.created_at)
        self.assertIsNotNone(self.am_1.updated_at)

    def test_type_attr_base(self):
        self.assertEqual(type(self.am_1.id), str)
        self.assertEqual(type(self.am_1.created_at), datetime)
        self.assertEqual(type(self.am_1.updated_at), datetime)

    def test_attr(self):
        self.assertEqual(self.am_1.name, "Kitchen")

    def test_no_arg(self):
        self.assertEqual(self.am_2.name, "")

    def test_type_args(self):
        self.assertEqual(type(self.am_1.name), str)
        self.assertEqual(type(self.am_2.name), str)

if __name__ == '__main__':
    unittest.main()
