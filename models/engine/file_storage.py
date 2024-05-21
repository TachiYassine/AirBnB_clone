#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os


class FileStorage:
    """Class for storing and retrieving data"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f, ensure_ascii=False)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

    def reload(self):
        """Reloads the stored objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        filepath = FileStorage.__file_path
        data = FileStorage.__objects
        if os.path.exists(filepath):
            try:
                with open(filepath) as f:
                    loaded_data = json.load(f)
                for key, value in loaded_data.items():
                    # Instantiate objects based on class names
                    if "BaseModel" in key:
                        data[key] = BaseModel(**value)
                    elif "User" in key:
                        data[key] = User(**value)
                    elif "Place" in key:
                        data[key] = Place(**value)
                    elif "State" in key:
                        data[key] = State(**value)
                    elif "City" in key:
                        data[key] = City(**value)
                    elif "Amenity" in key:
                        data[key] = Amenity(**value)
                    elif "Review" in key:
                        data[key] = Review(**value)
            except json.decoder.JSONDecodeError:
                # Handle invalid JSON data
                data.clear()  # Initialize to empty dictionary

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            "State": {
                "name": str
            },
            "City": {
                "state_id": str,
                "name": str
            },
            "Amenity": {
                "name": str
            },
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }
        return attributes

    @classmethod
    def get_file_path(cls):
        """Returns the file path"""
        return cls.__file_path

    @classmethod
    def get_objects(cls):
        """Returns the objects dictionary"""
        return cls.__objects
