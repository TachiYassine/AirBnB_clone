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
        pass

    def __str__(self) -> str:
        """
        This method returns a string representation of the instance:
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        pass

    def save(self) -> None:
        """
        This method updates the public instance attribute updated_at
        with the current datetime and saves the instance.
        """
        pass

    def to_dict(self) -> dict:
        """
        This method returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        pass
