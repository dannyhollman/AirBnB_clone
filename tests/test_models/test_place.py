#!/usr/bin/python3
""" unittest for Place class """
import unittest
from models.place import Place


class test_place(unittest.TestCase):
    """ class to test Place """

    def test_place(self):
        """ test Place class """
        test = Place()
        self.assertIsInstance(test, Place)

    def test_city_id(self):
        """ test city_id attribute """
        test = Place()
        test.city_id = "City.12345"
        self.assertEqual(test.city_id, "City.12345")

    def test_user_id(self):
        """ test user_id attribute """
        test = Place()
        test.user_id = "User.12345"
        self.assertEqual(test.user_id, "User.12345")

    def test_name(self):
        """ test name attribute """
        test = Place()
        test.name = "Holberton School"
        self.assertEqual(test.name, "Holberton School")

    def test_description(self):
        """ test description attribute """
        test = Place()
        test.description = "Software engineering school"
        self.assertEqual(test.description, "Software engineering school")

    def test_number_rooms(self):
        """ test number_rooms attribute """
        test = Place()
        test.number_rooms = 10
        self.assertEqual(test.number_rooms, 10)

    def test_number_bathrooms(self):
        """ test number_bathrooms attribute """
        test = Place()
        test.number_bathrooms = 1
        self.assertEqual(test.number_bathrooms, 1)

    def test_max_guest(self):
        """ test max_guest attribute """
        test = Place()
        test.max_guest = 50
        self.assertEqual(test.max_guest, 50)

    def test_price_by_night(self):
        """ test price_by_night attribute """
        test = Place()
        test.price_by_night = 1000
        self.assertEqual(test.price_by_night, 1000)

    def test_latitude(self):
        """ test latitude attribute """
        test = Place()
        test.latitude = 1.234
        self.assertEqual(test.latitude, 1.234)

    def test_longitude(self):
        """ test longitude attribute """
        test = Place()
        test.longitude = 2.345
        self.assertEqual(test.longitude, 2.345)

    def test_amenity_ids(self):
        test = Place()
        test.amenity_ids = ["Amenity.12345", "Amenity.23456"]
        self.assertListEqual(test.amenity_ids, ["Amenity.12345",
                                                "Amenity.23456"])
