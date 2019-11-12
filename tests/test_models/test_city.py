#!/usr/bin/python3
""" Tests for City instances """


from models.city import City
import unittest


class test_city(unittest.TestCase):
    """ class to test City """
    def test_city(self):
        """ test City class """
        test = City()
        self.assertIsInstance(test, City)

    def test_id(self):
        """ test id attribute """
        test = City()
        test.state_id = test.id
        self.assertEqual(test.state_id, test.id)

    def test_id_type(self):
        """ test id type """
        test = City()
        test.state_id = test.id
        self.assertEqual(type(test.state_id), str)

    def test_diff_ids(self):
        """ test if ids are different """
        test = City()
        test2 = City()
        assert test.id is not test2.id

    def test_kwargs(self):
        """ test dictionary for kwargs """
        test = City()
        _dict = test.to_dict()
        test2 = City(**_dict)
        _dict2 = test2.to_dict()
        self.assertDictEqual(_dict, _dict2)

    def test_name(self):
        """ test name attribute """
        test = City()
        test.name = "New Haven"
        self.assertEqual(test.name, "New Haven")

    def test_dic(self):
        """ test initialization with dictionary """
        test = City()
        dic = test.to_dict()
        dic.update(name="New Haven")
        test2 = City(**dic)
        self.assertEqual(test2.name, "New Haven")
