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
import models


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

        If keyword arguments are provided, they are used to set the instance attributes.
        Otherwise, default values are used for id, created_at, and updated_at.

        The Args we'll be using :
            *args: Variable length argument list (it was not used).
            **kwargs: Arbitrary keyword arguments for instance attributes.

        The Attributes we'll be using:
            id (str): Unique identifier for the instance.
            created_at (datetime): Timestamp when the instance was created.
            updated_at (datetime): Timestamp when the instance was last updated.

        """

        def parse_datetime(date_str: str) -> datetime:
            """
            Using this method we will avoid repeating the same code line
            and will help us Parse a datetime string into a datetime object.

            The Args used :
                date_str: String representation of the datetime.

            What this method Returns:
                A datetime object.
            """
            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at":
                    self.__dict__["created_at"] = parse_datetime(value)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = parse_datetime(value)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
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
        models.storage.save()

    def to_dict(self) -> dict:
        """
        This method returns a dictionary containing all keys/values
        of __dict__ of the instance.

        What this method Returns:
            dict: Dictionary representation of the instance.
        """
        # Create a copy of __dict__ to ensure only instance attributes set are returned
        my_dict = self.__dict__.copy()
        # Add __class__ key with the class name of the object
        my_dict["__class__"] = type(self).__name__
        # Convert created_at and updated_at to string object in ISO format
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()

        return my_dict
