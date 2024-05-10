#!/usr/bin/python3

import json

class FileStorage:

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects[type(obj).__name__ + "." + obj.id] = obj.to_dict()
    
    def save(self):
        with open(self.__file_path, "w+") as jsonFile:
            jsonFile.write(json.dumps(self.__objects))
        
    def reload(self):
        try:
            with open(self.__file_path, "r") as jsonFile:
                self.__objects = json.loads(jsonFile.read())
        except FileNotFoundError:
            pass
    
