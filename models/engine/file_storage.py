#!/usr/bin/python3

import json
import os


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__class__.__objects

    def new(self, obj):
        self.__class__.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):

        with open(self.__class__.__file_path, "w") as jsonFile:
            obj_to_dict_list = []
            for key, obj in self.__class__.__objects.items():
                obj_to_dict = {}
                obj_to_dict[key] = obj.to_dict()
                obj_to_dict_list.append(obj_to_dict)
            jsonFile.write(json.dumps(obj_to_dict_list))    

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User

        try:
            with open(self.__class__.__file_path, "r") as jsonFile:
                dicts_to_obj_list = json.loads(jsonFile.read())
                for dicts in dicts_to_obj_list:
                    for key, value in dicts.items():
                        model_name = key.split(".")[0]
                        if model_name == "BaseModel":
                            self.__class__.__objects[key] = BaseModel(**value)
                        elif model_name == "User":
                            self.__class__.__objects[key] = User(**value)
        except:
            pass
