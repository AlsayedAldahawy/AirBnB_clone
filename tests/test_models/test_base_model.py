#!/usr/bin/python3

import unittest
from uuid import uuid4
from io import StringIO
from contextlib import redirect_stdout
import sys
from models.base_model import BaseModel
from datetime import datetime, timedelta

class TestBaseModel(unittest.TestCase):
    """
    Test class for the BaseModel class.

    This class contains unit tests for various aspects of the BaseModel class.
    """
    def test_initialization(self):
        """
        Test the initialization of BaseModel instances.

        - Checks the uniqueness of the 'id' attribute.
        - Verifies that the 'id' attribute value is a string.
        - Validates the 'created_at' and 'updated_at' attributes.
        """
        model_1 = BaseModel()
        model_2 = BaseModel()

        # check the unique id attribute
        self.assertNotEqual(model_1.id, model_2.id)
        self.assertNotEqual(model_1.id, model_2.id, str(uuid4()))

        # check that id attribute value is string
        self.assertIsInstance(model_1.id, str)
        self.assertIsInstance(model_2.id, str)

        # check created_at attribute value
        self.assertAlmostEqual(model_1.created_at, datetime.now(), delta=timedelta(seconds=1))
        self.assertAlmostEqual(model_2.created_at, datetime.now(), delta=timedelta(seconds=1))

        # check created_at attribute type
        self.assertIsInstance(model_1.created_at, datetime)
        self.assertIsInstance(model_2.created_at, datetime)

        # check updated_at attribute value
        self.assertAlmostEqual(model_1.updated_at, datetime.now(), delta=timedelta(seconds=1))
        self.assertAlmostEqual(model_2.updated_at, datetime.now(), delta=timedelta(seconds=1))

        # check updated_at attribute type
        self.assertIsInstance(model_1.updated_at, datetime)
        self.assertIsInstance(model_2.updated_at, datetime)

    def test_attributes_changing(self):
        """
        Test changing attributes of BaseModel instances.

        - Checks forced values for 'id', 'created_at', and 'updated_at' attributes.
        """
        model_1 = BaseModel()
        model_2 = BaseModel()

        model_1.id = "abc123"
        model_2.id = "abc123"

        # check forced values to id attribute
        self.assertEqual(model_1.id, model_2.id, "abc123")

        model_1.created_at = datetime.now()
        model_2.created_at = datetime.now()

        # check forced values to created_at attribute
        self.assertAlmostEqual(model_1.created_at, datetime.now(), delta=timedelta(1))
        self.assertAlmostEqual(model_2.created_at, datetime.now(), delta=timedelta(1))

        model_1.updated_at = datetime.now()
        model_2.updated_at = datetime.now()

        # check forced values to created_at attribute
        self.assertAlmostEqual(model_1.updated_at, datetime.now(), delta=timedelta(1))
        self.assertAlmostEqual(model_2.updated_at, datetime.now(), delta=timedelta(1))
    
    def test_str(self):
        """
        Test the __str__ method of BaseModel.

        Verifies that the string representation of BaseModel matches the expected format.
        """
        model_1 = BaseModel()
        
        self.assertEqual(str(model_1), f"[BaseModel] ({model_1.id}) {model_1.__dict__}")

    def test_save(self):
        """
        Test the save method of BaseModel.

        - Checks if the 'updated_at' attribute changes after calling save().
        """

        obj1 = BaseModel()
        updated1 = obj1.updated_at
        obj1.save()

        self.assertNotEqual(updated1, obj1.updated_at)
        self.assertAlmostEqual(obj1.updated_at, datetime.now(), delta=timedelta(seconds=1))
    
    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel.

        Verifies that the dictionary representation of BaseModel matches the expected format.
        """
        obj1 = BaseModel()

        dict_1 = obj1.to_dict()
        dict_2 = dict(obj1.__dict__)
        dict_2["__class__"] = str(type(obj1).__name__)
        dict_2["created_at"] = obj1.created_at.isoformat()
        dict_2["updated_at"] = obj1.updated_at.isoformat()

        self.assertEqual(dict_1, dict_2)
       

    def test_checking_for_docstring_BaseModel(self):
        """
        Test if docstrings are present for BaseModel and its methods.

        Ensures that docstrings exist for __init__, __str__, save, and to_dict methods.
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_init_kwargs(self):
        """
        Test BaseModel initialization with kwargs.

        Verifies that initializing a BaseModel instance with its dictionary representation
        results in an equivalent object.
        """

        obj1 = BaseModel()
        dict_1 = obj1.to_dict()
        obj2 = BaseModel(**dict_1)

        self.assertEqual(obj1.id, obj2.id)
        self.assertEqual(obj1.created_at, obj2.created_at)
        self.assertEqual(obj1.updated_at, obj2.updated_at)
