#!/usr/bin/python3
""" Unit tests State class """
from models.state import State
import unittest
from datetime import datetime


class TestState(unittest.TestCase):
    """ Unit tests State class """

    def setUp(self):
        self.state_1 = State()
        self.state_1.name = "California"
        self.state_2 = State()

    def test_attr_base(self):
        self.assertIsNotNone(self.state_1.id)
        self.assertIsNotNone(self.state_1.created_at)
        self.assertIsNotNone(self.state_1.updated_at)

    def test_type_attr_base(self):
        self.assertEqual(type(self.state_1.id), str)
        self.assertEqual(type(self.state_1.created_at), datetime)
        self.assertEqual(type(self.state_1.updated_at), datetime)

    def test_attr(self):
        self.assertEqual(self.state_1.name, "California")

    def test_no_arg(self):
        self.assertEqual(self.state_2.name, "")

    def test_type_args(self):
        self.assertEqual(type(self.state_1.name), str)
        self.assertEqual(type(self.state_2.name), str)

if __name__ == '__main__':
    unittest.main()
