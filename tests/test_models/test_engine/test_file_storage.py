#!/usr/bin/python3

"""
Unittest for FileStorage class.
"""

import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class FileStorage_Test(unittest.TestCase):
    """Tests for File Storge class."""

    def setUp(self):
        """Set up"""
        pass

    def tearDown(self):
        """Tear down"""
        pass

    def test_00_private_attrs(self):
        """Validate attributes are private."""
        fs = FileStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

    def test_01_storage_all(self):
        """Tests the all method"""
        fs = FileStorage()
        self.assertEqual(type(fs.all()), dict)

        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()
        fs.new(b1)
        fs.new(b2)
        fs.new(b3)
        obj_dict = fs.all()
        self.assertEqual(type(obj_dict), dict)
        self.assertFalse(obj_dict == {})
        self.assertTrue("BaseModel.{}".format(b1.id) in obj_dict)
        self.assertTrue("BaseModel.{}".format(b2.id) in obj_dict)
        self.assertTrue("BaseModel.{}".format(b3.id) in obj_dict)

    def test_02_new(self):
        """Tests the new method"""
        fs = FileStorage()
        fs.new(BaseModel())
        self.assertTrue(fs.all())

        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))
        self.assertEqual(type(b.id), str)

    def test_03_save(self):
        """Tests the save method"""
        fs = FileStorage()
        b = BaseModel()
        fs.new(b)
        fs.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_04_reload(self):
        """Test the reload method."""
        fs = FileStorage()
        b = BaseModel()
        key = "BaseModel" + '.' + b.id
        fs.new(b)
        fs.save()
        fs.reload()
        self.assertTrue(fs.all()[key])
        fs.all()

    def test_05_attributs(self):
        """Test attributs"""
        fs = FileStorage()
        fs.__file_path = "file2.json"

    def test_new(self):
        """Tests the new function"""
        s1 = FileStorage()
        s1._FileStorage__objects = {}
        d1 = {}
        m1 = BaseModel()
        s1.new(m1)
        m2 = User()
        s1.new(m2)
        d1["BaseModel." + m1.id] = m1
        d1["User." + m2.id] = m2
        t1 = s1.all()
        self.assertDictEqual(t1, d1)

if __name__ == '__main__':
    unittest.main()
