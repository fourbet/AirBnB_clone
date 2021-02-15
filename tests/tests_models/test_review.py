#!/usr/bin/python3
""" Unit tests Review Class """
from models.review import Review
from models.user import User
from models.place import Place
import unittest
from datetime import datetime


class TestPlace(unittest.TestCase):
    """ Unit tests Review Class """

    def setUp(self):
        self.place = Place()
        self.user = User()
        self.rev_1 = Review()
        self.rev_1.place_id = self.place.id
        self.rev_1.user_id = self.user.id
        self.rev_1.text = "Nice"
        self.rev_2 = Place()

    def test_attr_base(self):
        self.assertIsNotNone(self.rev_1.id)
        self.assertIsNotNone(self.rev_1.created_at)
        self.assertIsNotNone(self.rev_1.updated_at)

    def test_type_attr_base(self):
        self.assertEqual(type(self.rev_1.id), str)
        self.assertEqual(type(self.rev_1.created_at), datetime)
        self.assertEqual(type(self.rev_1.updated_at), datetime)

    def test_attr(self):
        self.assertEqual(self.rev_1.text, "Nice")
        self.assertEqual(self.rev_1.place_id, self.place.id)
        self.assertEqual(self.rev_1.user_id, self.user.id)

    def test_no_arg(self):
        self.assertEqual(self.rev_2.name, "")

    def test_type_args(self):
        self.assertEqual(type(self.rev_2.name), str)

if __name__ == '__main__':
    unittest.main()