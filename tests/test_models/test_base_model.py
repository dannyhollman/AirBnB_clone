#!/usr/bin/python3
""" Unit test for BaseModel """
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ class to test BaseModel """
    def test_BaseModel(self):
        """ test BaseModel """
        test = BaseModel()
        self.assertIsInstance(test, BaseModel)

    def test_id(self):
        """ test if id is valid UUID """
        test = BaseModel()
        try:
            uuid.UUID(str(test.id))
            id_test = True
        except:
            id_test = False
        self.assertTrue(id_test)

    def test_id_unique(self):
        """ test if id is unique """
        test = BaseModel()
        test2 = BaseModel()
        self.assertNotEqual(test.id, test2.id)

    def test_created_at(self):
        """ test if created_at is datetime object """
        test = BaseModel()
        self.assertIsInstance(test.created_at, datetime)

    def test_updated_at(self):
        """ test if updated_at is datetime object """
        test = BaseModel()
        self.assertIsInstance(test.updated_at, datetime)

    def test_to_dict(self):
        """ test to_dict function """
        test = BaseModel()
        dic = test.to_dict()
        self.assertIsInstance(dic, dict)

    def test_kwargs(self):
        """ test initializing class from dictionary """
        test = BaseModel()
        dic = test.to_dict()
        test2 = BaseModel(**dic)
        dic2 = test2.to_dict()
        self.assertDictEqual(dic, dic2)

