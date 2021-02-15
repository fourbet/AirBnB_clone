#!/usr/bin/python3

"""
Unittest for the Console class
"""

import unittest
import sys
from unittest.mock import patch
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from console import HBNBCommand
from io import StringIO
import re


class Console_Test(unittest.TestCase):
    """Tests for the console."""

    def setUp(self):
        """Set up tests."""
        pass

    def test_01_quit(self):
        """Test quit"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_01_EOF(self):
        """Test EOF"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_06_show(self):
        """Test show"""
        b = BaseModel()
        b_id = b.id
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(" + b_id + ")")
            self.assertIn('BaseModel', f.getvalue())

        s = State()
        s_id = s.id
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("State.show(" + s_id + ")")
            self.assertIn('State', f.getvalue())

        u = User()
        u_id = u.id
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.show(" + u_id + ")")
            self.assertIn('User', f.getvalue())

        a = Amenity()
        a_id = a.id
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.show(" + a_id + ")")
            self.assertIn('Amenity', f.getvalue())

        r = Review()
        r_id = r.id
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Review.show(" + r_id + ")")
            self.assertIn('Review', f.getvalue())

        c = City()
        c_id = c.id
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("City.show(" + c_id + ")")
            self.assertIn('City', f.getvalue())

        p = Place()
        p_id = p.id
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Place.show(" + p_id + ")")
            self.assertIn('Place', f.getvalue())

if __name__ == '__main__':
    unittest.main()
