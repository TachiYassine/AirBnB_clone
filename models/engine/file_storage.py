#!/usr/bin/python3
"""
Module file_storage.py
Contains a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances.
"""

import os.path
import json
import os


class FileStorage:
    """
    A class to manage serialization and deserialization
    of objects to/from a JSON file.
    """

    # Default file path for JSON serialization
    __file_path = "file.json"
    # Dictionary to store serialized objects
    __objects = {}

    def all(self):
        """
        Returns the dictionary of serialized objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary __objects.
        """
        if obj:
            name = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[name] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        my_dict = {}
        for key, val in self.__objects.items():
            my_dict[key] = val.to_dict()

        with open(self.__file_path, "w") as my_file:
            json.dump(my_dict, my_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        my_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        if not os.path.isfile(self.__file_path):
            return

        with open(self.__file_path, "r") as file_path:
            objects = json.load(file_path)
            self.__objects = {}
            for key in objects:
                name = key.split(".")[0]
                self.__objects[key] = my_dict[name](**objects[key])
