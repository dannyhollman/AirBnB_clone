#!/usr/bin/python3
""" Tests for Review instances """

from models.user import User
from models.review import Review
import unittest


class test_review(unittest.TestCase):
    """ class to test Review """
    def test_review(self):
        """ test review class """
        test = Review()
        self.assertIsInstance(test, Review)

    def test_diff_id(self):
        """ test if ids are different """
        test = Review()
        test2 = Review()
        self.assertNotEqual(test.id, test2.id)

    def test_place_id(self):
        """ test place id """
        test = Review()
        test.place_id = test.id
        self.assertEqual(test.place_id, test.id)

    def test_user_id(self):
        """ test user id """
        test = Review()
        user = User()
        test.user_id = user.id
        self.assertEqual(test.user_id, user.id)

    def test_text(self):
        """ test text string """
        test = Review()
        test.text = "Highly recommend 9/10"
        self.assertEqual(test.text, "Highly recommend 9/10")

    def test_place_id_type(self):
        """ test place id type """
        test = Review()
        test.place_id = test.id
        self.assertEqual(type(test.place_id), str)

    def test_user_id_type(self):
        """ test user id type """
        test = Review()
        user = User()
        test.user_id = user.id
        self.assertEqual(type(test.user_id), str)

    def test_text_type(self):
        """ test text string type """
        test = Review()
        test.text = "This place was nasty"
        self.assertEqual(type(test.text), str)

    def test_dic(self):
        """ test initialization with dictionary """
        test = Review()
        _dict = test.to_dict()
        _dict.update(place_id=test.id)
        test2 = Review(**_dict)
        self.assertEqual(test2.place_id, test.id)

    def test_kwargs(self):
        """ test kwargs for class review """
        test = Review()
        _dict = test.to_dict()
        test2 = Review(**_dict)
        _dict2 = test2.to_dict()
        self.assertDictEqual(_dict, _dict2)
