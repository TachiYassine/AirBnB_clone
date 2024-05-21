#!/usr/bin/python3
""" This py file will make all the unit tests
for our class State and its objects"""

import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):

    def setUp(self):
        # In order to test our class we need to Initialize a state instance
        self.state = State()

    def tearDown(self):
        """Deletes the State instance after each test"""
        del self.state

    def test_instance(self):
        """TVerifies the instance and attributes,
        ensuring they exist and are of the correct type."""
        self.assertIsInstance(self.state, State)
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertTrue(hasattr(self.state, "name"))
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)
        self.assertIsInstance(self.state.name, str)

    def test_str(self):
        """Test the __str__ method of State."""
        string = str(self.state)
        self.assertIn("[State]", string)
        self.assertIn(f"({self.state.id})", string)
        self.assertIn("name", string)

    def test_to_dict(self):
        """Ensures the to_dict method returns a dictionary
        with the expected keys and values"""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIn("__class__", state_dict)
        self.assertEqual(state_dict["__class__"], "State")

    def test_from_dict(self):
        """Test instantiation from a dictionary."""
        state_dict = self.state.to_dict()
        new_state = State(**state_dict)
        self.assertEqual(self.state.id, new_state.id)
        self.assertEqual(self.state.created_at, new_state.created_at)
        self.assertEqual(self.state.updated_at, new_state.updated_at)
        self.assertEqual(self.state.name, new_state.name)


if __name__ == "__main__":
    unittest.main()
