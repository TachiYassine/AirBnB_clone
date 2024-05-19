#!/usr/bin/python3
"""
The class BaseModel will be the backbone of our project
and will have all the common aspects (attributes, methods)
that the other classes share. It will also be responsible for
the initialization and conversion (JSON <=> Python), mainly called
serialization and deserialization, and will
have other methods that will be explained later.
"""

from uuid import uuid4
from datetime import datetime
from models import storage
import uuid
import json
import sys
import os.path


class BaseModel:
    """
    The BaseModel class serves as the backbone of our project,
    encapsulating common attributes and methods shared by other classes.
    It is responsible for initialization, serialization, deserialization,
    and other functionalities to be explained later.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        This is the constructor method for the BaseModel class,
        it initializes the instance variables and won't return any value.
        """
        if kwargs:
            dtf = '%Y-%m-%dT%H:%M:%S.%f'
            kwargs_copy = kwargs.copy()
            del kwargs_copy["__class__"]
            for key in kwargs_copy:
                if ("created_at" == key or "updated_at" == key):
                    kwargs_copy[key] = datetime.strptime(kwargs_copy[key], dtf)
            self.__dict__ = kwargs_copy
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """
        This method returns a string representation of the instance:
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return ('[{}] ({}) {}'.format(
            self.__class__.__name__,
            self.id,
            self.__class__.__dict__))

    def save(self) -> None:
        """
        This method updates the public instance attribute updated_at
        with the current datetime and saves the instance.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """
        This method returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        result_dict = {}
        result_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, (datetime,)):
                result_dict[key] = value.isoformat()
            else:
                result_dict[key] = value
        return result_dict

    def to_json(self):
        """
        Returns a JSON serializable dictionary containing all key-value pairs
        of __dict__ of the instance.
        """
        json_dict = self.__dict__.copy()
        dt_format = '%Y-%m-%dT%H:%M:%S.%f'
        json_dict['created_at'] = self.created_at.strftime(dt_format)
        json_dict['__class__'] = str(self.__class__.__name__)
        if hasattr(self, 'updated_at'):
            json_dict['updated_at'] = self.updated_at.strftime(dt_format)
        return json_dict
