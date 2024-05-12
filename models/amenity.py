#!/usr/bin/python3

"""
Amenity Module

This module defines the Amenity class, which inherits from BaseModel. It represents an amenity with a name attribute.
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
