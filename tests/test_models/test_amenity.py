#!/usr/bin/python3
""" Unit tests Amenity class """
from models.amenity import Amenity
import unittest
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """ Unit tests Amenity class """

    def setUp(self):
        """ Initialization """
        self.am_1 = Amenity()
        self.am_1.name = "Kitchen"
        self.am_2 = Amenity()

    def test_attr_base(self):
        """ Test attribut BaseModel """
        self.assertIsNotNone(self.am_1.id)
        self.assertIsNotNone(self.am_1.created_at)
        self.assertIsNotNone(self.am_1.updated_at)

    def test_type_attr_base(self):
        """ Test type attribut BaseModel """
        self.assertEqual(type(self.am_1.id), str)
        self.assertEqual(type(self.am_1.created_at), datetime)
        self.assertEqual(type(self.am_1.updated_at), datetime)

    def test_attr(self):
        """ Test attribut Amenity class """
        self.assertEqual(self.am_1.name, "Kitchen")

    def test_no_arg(self):
        """ Test Amenity class with no attribut """
        self.assertEqual(self.am_2.name, "")

    def test_type_args(self):
        """ Test type attribut Amenity """
        self.assertEqual(type(self.am_1.name), str)
        self.assertEqual(type(self.am_2.name), str)

if __name__ == '__main__':
    unittest.main()
