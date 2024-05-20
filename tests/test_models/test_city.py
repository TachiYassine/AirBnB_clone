#!/usr/bin/python3
""" This py file will make all the unit tests
for our class City and its objects"""

import unittest
from models.city import City
from datetime import datetime


class MyCityTest(unittest.TestCase):

    def setUp(self):
        # In order to test our class we need to Initialize a City object
        self.city = City()

    def test_for_attributes_existence(self):
        """ Test the existence of our attributes """
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_for_attributes_types(self):
        """ Test the types of our attributes """
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_for_to_dict_method(self):
        """ Test the to_dict() method """
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['id'], self.city.id)
        self.assertEqual(city_dict['created_at'], self.city.created_at.isoformat())
        self.assertEqual(city_dict['updated_at'], self.city.updated_at.isoformat())
        self.assertEqual(city_dict['state_id'], self.city.state_id)
        self.assertEqual(city_dict['name'], self.city.name)


if __name__ == '__main__':
    unittest.main()
