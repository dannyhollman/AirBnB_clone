#!/usr/bin/python3
""" unittest for State class """
import unittest
from models.state import State


class test_state(unittest.TestCase):
    """ class to test State """
    def test_state(self):
        """ test State class """
        test = State()
        self.assertIsInstance(test, State)

    def test_name(self):
        """ test name attribute """
        test = State()
        test.name = "Connecticut"
        self.assertEqual(test.name, "Connecticut")

    def test_dic(self):
        """ test initialization with dictionary """
        test = State()
        dic = test.to_dict()
        dic.update(name="Connecticut")
        test2 = State(**dic)
        self.assertEqual(test2.name, "Connecticut")
