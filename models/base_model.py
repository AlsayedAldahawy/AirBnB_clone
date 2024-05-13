#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage

'''
    base_model.py module cintains the class BaseModel
'''


class BaseModel:
    """
    The 'BaseModel' class serves as a base class for other models in\
        the project.
    It provides common attributes and methods that can be inherited by\
        other classes.

    Attributes:
        id (str): A unique identifier generated using 'uuid4()'\
            (a version 4 UUID).
        created_at (datetime): A timestamp representing the creation date\
            and time (initialized with the current datetime).
        updated_at (datetime): A timestamp representing the last update date\
            and time (also initialized with the current datetime).

    Methods:
        __init__(self): Initializes the attributes ('id', 'created_at', and\
            'updated_at').
        __str__(self): Returns string representation of the object, including\
            its class name, ID, and other attributes.
        save(self): Updates the updated_at attribute with the current datetime.
        to_dict(self): Creates a dictionary representation of the object,\
            including class name and formatted timestamps.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the `BaseModel` instance.

        Attributes:
            id (str): A unique identifier generated using `uuid4()`.
            created_at (datetime): The timestamp representing the creation\
                date and time.
            updated_at (datetime): The timestamp representing the last update\
                date and time.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

        storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the `BaseModel` object.

        Returns:
            str: A formatted string containing class name, ID, and other\
                attributes.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Creates a dictionary representation of the object.

        Returns:
            dict: A dictionary containing all the key-value pairs\
                from __dict__.
        """
        attr_dict = dict(self.__dict__)
        attr_dict["__class__"] = str(type(self).__name__)
        attr_dict["created_at"] = self.created_at.isoformat()
        attr_dict["updated_at"] = self.updated_at.isoformat()
        return attr_dict
