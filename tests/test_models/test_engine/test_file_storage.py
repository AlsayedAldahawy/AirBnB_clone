#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage

class Test_attributes(unittest.TestCase):

    def test_filepath(self):

        obj = FileStorage()

        with self.assertRaises(AttributeError):
            getattr(obj, "_FileStorage.__file_path")
