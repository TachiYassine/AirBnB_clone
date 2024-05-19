#!/usr/bin/python3
"""
The class BaseModel will be the backbone of our project
and will have all the common aspects (attributes, methods)
that the other classes share. It will also be responsible for
the initialization and conversion (JSON <=> Python), mainly called
serialization and deserialization, and will
have other methods that will be explained later.
"""

import uuid
from datetime import datetime
from models import storage


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
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """
        This method returns a string representation of the instance:
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

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
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
