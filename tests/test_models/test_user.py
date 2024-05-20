#!/usr/bin/python3
""" This py file will make all the unit tests
for our class User and its objects"""

import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):

    def test_for_attributes_existence(self):
        """ Test the existence of our attributes """
        new_user = User()
        self.assertTrue(hasattr(new_user, "id"))
        self.assertTrue(hasattr(new_user, "created_at"))
        self.assertTrue(hasattr(new_user, "updated_at"))
        self.assertTrue(hasattr(new_user, "email"))
        self.assertTrue(hasattr(new_user, "password"))
        self.assertTrue(hasattr(new_user, "first_name"))
        self.assertTrue(hasattr(new_user, "last_name"))

    def test_for_attributes_types(self):
        """ Test the types of our attributes """
        new_user = User()
        self.assertIsInstance(new_user.id, str)
        self.assertIsInstance(new_user.created_at, datetime)
        self.assertIsInstance(new_user.updated_at, datetime)
        self.assertIsInstance(new_user.email, str)
        self.assertIsInstance(new_user.password, str)
        self.assertIsInstance(new_user.first_name, str)
        self.assertIsInstance(new_user.last_name, str)

    def test_for_to_dict_method(self):
        """ Test the to_dict() method """
        new_user = User()
        user_dict = new_user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], new_user.id)
        self.assertEqual(user_dict['created_at'], new_user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'], new_user.updated_at.isoformat())
        self.assertEqual(user_dict['email'], new_user.email)
        self.assertEqual(user_dict['password'], new_user.password)
        self.assertEqual(user_dict['first_name'], new_user.first_name)
        self.assertEqual(user_dict['last_name'], new_user.last_name)


if __name__ == '__main__':
    unittest.main()
