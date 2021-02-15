#!/usr/bin/python3
""" Unit tests User class """
from models.user import User
import unittest
from datetime import datetime


class TestUser(unittest.TestCase):
    """ Unit tests User class """

    def setUp(self):
        """ Initialization """
        self.user_1 = User()
        self.user_1.email = "holberton@school.com"
        self.user_1.password = "***"
        self.user_1.first_name = "Max"
        self.user_1.last_name = "James"
        self.user_2 = User()

    def test_attr_base(self):
        """ Test attribut BaseModel """
        self.assertIsNotNone(self.user_1.id)
        self.assertIsNotNone(self.user_1.created_at)
        self.assertIsNotNone(self.user_1.updated_at)

    def test_type_attr_base(self):
        """ Test type attribut BaseModel """
        self.assertEqual(type(self.user_1.id), str)
        self.assertEqual(type(self.user_1.created_at), datetime)
        self.assertEqual(type(self.user_1.updated_at), datetime)

    def test_attr(self):
        """ Test attribut User class """
        self.assertEqual(self.user_1.first_name, "Max")
        self.assertEqual(self.user_1.last_name, "James")
        self.assertEqual(self.user_1.email, "holberton@school.com")
        self.assertEqual(self.user_1.password, "***")

    def test_no_arg(self):
        """ Test User class with no attribut """
        self.assertEqual(self.user_2.first_name, "")
        self.assertEqual(self.user_2.last_name, "")
        self.assertEqual(self.user_2.email, "")
        self.assertEqual(self.user_2.password, "")

    def test_type_args(self):
        """ Test type attribut User """
        self.assertEqual(type(self.user_1.first_name), str)
        self.assertEqual(type(self.user_2.first_name), str)

if __name__ == '__main__':
    unittest.main()
