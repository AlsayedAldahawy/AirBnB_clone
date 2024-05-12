#!/usr/bin/python3

"""
Review Module

This module defines the Review class, which inherits from BaseModel. It represents a review with attributes for place ID, user ID, and text.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Represents a review.

    Attributes:
        place_id (str): The ID of the associated place.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
