#!/usr/bin/python3

"""
User Module

This module defines the User class with attributes for email, password,\
    first name, and last name.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User inherited from BaseModel Class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
