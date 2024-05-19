#!/usr/bin/python3
"""
This py file will make all the unit tests
for our class BaseModel and its objects
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        # In order to test our class we need to Initialize a BaseModel object for testing
        self.base_model = BaseModel()

    def test_init_method(self):
        # Test if id, created_at, and updated_at are initialized correctly
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_method(self):
        # Test the __str__() method
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        # Test the save() method
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

        # Additional checks

        # verifies that the id attribute of the BaseModel instance is of type str, ensuring that it is a string value.
        self.assertIsInstance(self.base_model.id, str)
        """
        checks that the created_at attribute of the BaseModel instance 
        is an instance of the datetime class, ensuring that it represents a valid timestamp
        """
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

        first_dict = self.base_model.to_dict()

        self.base_model.first_name = "Second"
        self.base_model.save()
        sec_dict = self.base_model.to_dict()

        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])

    def test_to_dict_method(self):
        # Test the to_dict() method
        obj_dict = self.base_model.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], self.base_model.id)
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())

    def test_my_base_model(self):
        """
        Test complementary and specific attribute assignments and
        their reflection in the dictionary and regarding our Base Module instance
        """
        # Set some attributes for our tests
        self.base_model.name = "Holberton"
        self.base_model.my_number = 89

        # Check if the attributes are correctly set before saving
        self.assertEqual(self.base_model.name, "Holberton")
        self.assertEqual(self.base_model.my_number, 89)

        # Save the instance
        self.base_model.save()

        # Convert the instance to a dictionary
        my_model_json = self.base_model.to_dict()

        # Check if the saved attributes are correctly reflected in the dictionary
        self.assertEqual(my_model_json['name'], "Holberton")
        self.assertEqual(my_model_json['my_number'], 89)


if __name__ == '__main__':
    unittest.main()
