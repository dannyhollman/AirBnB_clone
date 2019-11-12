#!/usr/bin/python3
""" Tests for Amenity instances """

from models.amenity import Amenity
import unittest


class test_amenity(unittest.TestCase):
    """ Class to test Amenity """
    def test_amenity(self):
        """ test Amenity class """
        test = Amenity()
        self.assertIsInstance(test, Amenity)

    def test_name(self):
        """ test name attribute """
        test = Amenity()
        test.name = "Hot Tub"
        self.assertEqual(test.name, "Hot Tub")

    def test_name_type(self):
        """ test name type """
        test = Amenity()
        test.name = "Butler"
        self.assertEqual(type(test.name), str)

    def test_diff_ids(self):
        """ test if ids are different """
        test = Amenity()
        test2 = Amenity()
        assert test.id is not test2.id

    def test_kwargs(self):
        """ test dictionary for kwargs """
        test = Amenity()
        _dict = test.to_dict()
        test2 = Amenity(**_dict)
        _dict2 = test2.to_dict()
        self.assertDictEqual(_dict, _dict2)

    def test_dic(self):
        """ test name with dictionary """
        test = Amenity()
        _dict = test.to_dict()
        _dict.update(name="Mini Fridge")
        test2 = Amenity(**_dict)
        self.assertEqual(test2.name, "Mini Fridge")
