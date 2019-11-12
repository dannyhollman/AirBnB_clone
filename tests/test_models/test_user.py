#!/usr/bin/python3
import unittest
from models.user import User


class test_user(unittest.TestCase):
    def test_user(self):
        test = User()
        self.assertIsInstance(test, User)

    def test_user_email(self):
        test = User()
        test.email = "test@test.com"
        self.assertEqual(test.email, "test@test.com")

    def test_user_password(self):
        test = User()
        test.password = "password"
        self.assertEqual(test.password, "password")

    def test_user_first_name(self):
        test = User()
        test.first_name = "Betty"
        self.assertEqual(test.first_name, "Betty")

    def test_user_last_name(self):
        test = User()
        test.last_name = "Holberton"
        self.assertEqual(test.last_name, "Holberton")
