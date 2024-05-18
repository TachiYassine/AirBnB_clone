#!/usr/bin/python3
"""
The class BaseModel will be the back bone of our project 
and will have all the common aspects (attributes, methods) 
that the other classes share and will also be responsable for
the initialization and conversion (JSON <=> Python): mainely called
serialization and deserialization and will 
have other methods that will be explained later

"""

# This will allow us to directly use the datetime class and create datetime objects (dates and times)
from datetime import datetime

# Th3is will allow us to work with with Universally Unique Identifiers that are useful for generating identifiers (create unique IDs)
from uuid import uuid4

# This will allow us to have acces to our model "models" :contains definitions for classes, functions ... that we want to use
import models

class BaseModel:


    # This is the constructor method for the BaseModel class, it initializes the instance variables and won't return any value
    def __init__(self, *args, **kwargs) -> None:

    # This method to return a string representation of the instance: should print: [<class name>] (<self.id>) <self.__dict__>
    def __str__(self) -> str:

    # This method updates the public instance attribute updated_at with the current datetime and save the instance
    def save(self) -> None:

    # This method returns a dictionary containing all keys/values of __dict__ of the instance
    def to_dict(self) -> dict:

