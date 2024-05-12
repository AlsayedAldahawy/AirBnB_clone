#!/usr/bin/python3

"""
    file_storage.py module contains FileStorage Class
"""


import json


class FileStorage:
    """
    FileStorage Class

    This class manages the storage of objects in a JSON file. It provides\
        methods for saving, loading, and manipulating objects.

    Attributes:
        __file_path (str): The path to the JSON file where objects are stored.
        __objects (dict): A dictionary containing object instances, indexed by\
            their unique keys.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns all objects stored in the storage.

        Returns:
            dict: A dictionary of object instances.
        """
        return self.__class__.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj: An instance of a class.

        Returns:
            None
        """
        self.__class__.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Saves objects to the JSON file.

        Returns:
            None
        """
        with open(self.__class__.__file_path, "w") as jsonFile:
            obj_to_dict_list = []
            for key, obj in self.__class__.__objects.items():
                obj_to_dict = {}
                obj_to_dict[key] = obj.to_dict()
                obj_to_dict_list.append(obj_to_dict)
            jsonFile.write(json.dumps(obj_to_dict_list))

    def reload(self):
        """
        Reloads objects from the JSON file.

        Returns:
            None
        """
        from models.base_model import BaseModel
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.user import User

        cls_name_to_cls = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }

        try:
            with open(self.__class__.__file_path, "r") as jsonFile:

                dicts_to_obj_list = json.loads(jsonFile.read())

                for dicts in dicts_to_obj_list:
                    for key, value in dicts.items():
                        class_name = key.split(".")[0]
                        if class_name in cls_name_to_cls:
                            self.__class__.__objects[key] = cls_name_to_cls[
                                class_name](**value)

        except Exception:
            pass
