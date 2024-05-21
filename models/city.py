#!/usr/bin/python3
"""
This file is for declaring
and defining our City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class represents our City entity.

    Attributes:
        state_id (str): The ID of the state associated with the city.
        name (str): The name of the city.
    """

    def __init__(self, *args, **kwargs):
        """Initialize our City instance."""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
