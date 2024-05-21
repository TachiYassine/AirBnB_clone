#!/usr/bin/python3
"""
This file is for declaring
and defining our Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class represents our Review entity.

    Attributes:
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who created the review.
        text (str): The text content of the review.
    """

    def __init__(self, *args, **kwargs):
        """Initialize our Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
