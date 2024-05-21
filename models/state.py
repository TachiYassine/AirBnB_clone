#!/usr/bin/python3
"""
This file is for declaring
and defining our State class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
   This class represents our State entity.

   The Attributes we'll be using:
        name (str): The name of the state.

    Return:
        None
    """

    def __init__(self, *args, **kwargs):
        """ we will Initialize our State instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
