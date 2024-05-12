#!/usr/bin/python3

"""
State Module

This module defines the State class, which inherits from BaseModel.\
    It represents a state with a name attribute.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
