#!/usr/bin/python3
""" Unit tests Place Class """
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
import unittest
from datetime import datetime


class TestPlace(unittest.TestCase):
    """ Unit tests Place Class """

    def setUp(self):
        """ Initialization """
        self.city = City()
        self.user = User()
        self.amenity = Amenity()
        self.place_1 = Place()
        self.place_1.city_id = self.city.id
        self.place_1.user_id = self.user.id
        self.place_1.name = "Hostel"
        self.place_1.description = "Four stars"
        self.place_1.number_rooms = 56
        self.place_1.number_bathrooms = 50
        self.place_1.max_guest = 210
        self.place_1.price_by_night = 110
        self.place_1.latitude = 74.03
        self.place_1.longitude = 145.36
        self.place_1.amenity_ids = [self.amenity]
        self.place_2 = Place()

    def test_attr_base(self):
        """ Test attribut BaseModel """
        self.assertIsNotNone(self.place_1.id)
        self.assertIsNotNone(self.place_1.created_at)
        self.assertIsNotNone(self.place_1.updated_at)

    def test_type_attr_base(self):
        """ Test type attribut BaseModel """
        self.assertEqual(type(self.place_1.id), str)
        self.assertEqual(type(self.place_1.created_at), datetime)
        self.assertEqual(type(self.place_1.updated_at), datetime)

    def test_attr(self):
        """ Test attribut Place class """
        self.assertEqual(self.place_1.name, "Hostel")
        self.assertEqual(self.place_1.description, "Four stars")
        self.assertEqual(self.place_1.city_id, self.city.id)
        self.assertEqual(self.place_1.user_id, self.user.id)
        self.assertEqual(self.place_1.number_rooms, 56)
        self.assertEqual(self.place_1.number_bathrooms, 50)
        self.assertEqual(self.place_1.max_guest, 210)
        self.assertEqual(self.place_1.price_by_night, 110)
        self.assertEqual(self.place_1.latitude, 74.03)
        self.assertEqual(self.place_1.longitude, 145.36)

    def test_no_arg(self):
        """ Test Place class with no attribut """
        self.assertEqual(self.place_2.name, "")
        self.assertEqual(self.place_2.description, "")
        self.assertEqual(self.place_2.city_id, "")
        self.assertEqual(self.place_2.user_id, "")
        self.assertEqual(self.place_2.number_rooms, 0)
        self.assertEqual(self.place_2.number_bathrooms, 0)
        self.assertEqual(self.place_2.max_guest, 0)
        self.assertEqual(self.place_2.price_by_night, 0)
        self.assertEqual(self.place_2.latitude, 0.0)
        self.assertEqual(self.place_2.longitude, 0.0)
        self.assertEqual(self.place_2.amenity_ids, [])

    def test_type_args(self):
        """ Test type attribut Place """
        self.assertEqual(type(self.place_2.name), str)
        self.assertEqual(type(self.place_2.description), str)
        self.assertEqual(type(self.place_2.number_rooms), int)
        self.assertEqual(type(self.place_2.max_guest), int)
        self.assertEqual(type(self.place_2.price_by_night), int)
        self.assertEqual(type(self.place_2.latitude), float)
        self.assertEqual(type(self.place_2.longitude), float)

if __name__ == '__main__':
    unittest.main()
