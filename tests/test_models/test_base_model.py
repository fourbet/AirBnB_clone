#!/usr/bin/python3

"""
Unittest for BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Tests for BaseModel class
    """

    def setUp(self):
        """Set up"""
        self.base1 = BaseModel()

    def tearDown(self):
        """Tears down"""
        pass

    def test_00_class_type(self):
        """Test for correct class type"""
        b = BaseModel()
        self.assertEqual(b.__class__.__name__, "BaseModel")

    def test_01_no_args(self):
        """Test for no arguments passed"""
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_02_correct_types(self):
        """Test for correct types in args"""
        b = BaseModel()
        self.assertEqual(type(b.id), str)
        self.assertEqual(b.created_at.__class__.__name__, "datetime")
        self.assertEqual(b.updated_at.__class__.__name__, "datetime")

    def test_03_adding_extra_parameters(self):
        """Test for manually adding parameters"""
        b = BaseModel()
        b.first_name = "Ophelie"
        b.age = 24
        self.assertTrue(hasattr(b, "first_name"))
        self.assertTrue(hasattr(b, "age"))
        self.assertEqual(type(b.first_name), str)
        self.assertEqual(type(b.age), int)

    def test_04_to_dict(self):
        """Test to validate to_dict"""
        b = BaseModel()
        b.first_name = "Huy"
        b.age = 18
        d = b.to_dict()
        self.assertTrue('first_name' in d)
        self.assertTrue('age' in d)
        self.assertTrue('id' in d)
        self.assertTrue('created_at' in d)
        self.assertTrue('updated_at' in d)
        self.assertTrue('__class__' in d)

    def test_05_manual_kwargs(self):
        """Test for manually entering in kwargs"""
        b = BaseModel(id=uuid.uuid4,
                      created_at=datetime.now().isoformat(),
                      updated_at=datetime.now().isoformat(),
                      name="John",
                      age=89)
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "name"))

    def test_06_attr_not_none(self):
        """ Test attribut BaseModel """
        self.assertIsNotNone(self.base1.id)
        self.assertIsNotNone(self.base1.created_at)
        self.assertIsNotNone(self.base1.updated_at)

    def test_07_str_save(self):
        """ test methods save and str"""
        string = "[BaseModel] ({}) {}".format(self.base1.id, self.base1.__dict__)
        self.assertEqual(string, self.base1.__str__())
        self.base1.save()

if __name__ == '__main__':
    unittest.main()
