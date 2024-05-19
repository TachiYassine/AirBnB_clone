#!/usr/bin/python3
"""
Module file_storage
Contains a class FileStorage
that serializes instances to a JSON file and
deserializes JSON file to instances
"""
import os.path
import json
import os


class FileStorage:
    """
    A class for serializing instances to a JSON file
    and deserializing JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            name = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[name] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        my_dict = {}
        for keys, val in self.__objects.items():
            my_dict[keys] = val.to_dict()
        with open(self.__file_path, "w") as my_file:
            json.dump(my_dict, my_file)

    def reload(self):
    ''' Deserializes/loads the JSON file to __objects '''

    my_dict = {
        "BaseModel": BaseModel,
        # Add other class names here if needed
    }
    
    if not os.path.isfile(self.__file_path):
        return
    
    with open(self.__file_path, "r") as file_path:
        objects = json.load(file_path)
        self.__objects = {}
        for key in objects:
            name = key.split(".")[0]
            if name in my_dict:
                self.__objects[key] = my_dict[name](**objects[key])
