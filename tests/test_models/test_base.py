#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBase(unittest.TestCase):

    def test_attr(self):

        obj1 = BaseModel()
        obj2 = BaseModel()
        time = datetime.now()
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj1.created_at, obj2.created_at)

    def test_str(self):

        obj1 = BaseModel()
        
        self.assertEqual(str(obj1), f"[BaseModel] ({obj1.id}) {obj1.__dict__}")

    def test_save(self):
        obj1 = BaseModel()
        obj1.save()
        self.assertNotEqual(obj1.created_at, obj1.updated_at)
    
    def test_to_dict(self):
        obj1 = BaseModel()

        dict_1 = obj1.to_dict()
        dict_2 = dict(obj1.__dict__)
        dict_2["__class__"] = str(type(obj1).__name__)
        dict_2["created_at"] = obj1.created_at.isoformat()
        dict_2["updated_at"] = obj1.updated_at.isoformat()

        self.assertEqual(dict_1, dict_2)
