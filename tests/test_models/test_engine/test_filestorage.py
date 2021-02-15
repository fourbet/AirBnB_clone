#!/usr/bin/python3

"""
Unittest for FileStorage class.
"""

import unittest
import os
from models import storage
from models.base_model import BaseModel
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
        with self.assertRaises(AttributeError):
            print(fs.objects)
        with self.assertRaises(AttributeError):
            print(fs.file_path)



if __name__ == '__main__':
    unittest.main()
