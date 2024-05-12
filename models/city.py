#!/usr/bin/python3

"""
City Module

This module defines the City class, which inherits from BaseModel. It represents a city with attributes for state ID and name.
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    Represents a city.

    Attributes:
        state_id (str): The ID of the state associated with the city.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
