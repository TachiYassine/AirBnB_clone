#!/usr/bin/python3
"""
This file is for declaring
and defining our City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class represents our City entity.

    The Attributes we'll be using:
        state_id (str): The ID of the state associated with the city.
        name (str): The name of the city.

    Return:
        None
    """

    def __init__(self, *args, **kwargs):
        """we will Initialize our City instance."""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
