#!/usr/bin/python3
""" This py file will make all the unit tests
for our class Amenity and its objects"""

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):

    def setUp(self):
        # In order to test our class we need to Initialize an Amenity object
        self.amenity = Amenity()

    def test_for_attributes_existence(self):
        """ Test the existence of our attributes """
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_for_attributes_types(self):
        """ Test the types of our attributes """
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)
        self.assertIsInstance(self.amenity.name, str)

    def test_for_to_dict_method(self):
        """ Test the to_dict() method """
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], self.amenity.id)
        self.assertEqual(amenity_dict['created_at'], self.amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'], self.amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict['name'], self.amenity.name)

    def test_my_amenity(self):
        """ Test existence and types of attributes in a single method """
        new = Amenity()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "name"))
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.name, str)


if __name__ == '__main__':
    unittest.main()
