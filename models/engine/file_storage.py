#!/usr/bin/python3
"""
Save json
"""
import json
from models.base_model import BaseModel


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    classes = {
        "BaseModel": BaseModel
    }

    def __init__(self, *args, **kwargs):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        newjson = {}
        for key, value in self.__objects.items():
            newjson[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(newjson))

    def reload(self):
        dictnew = {}
        try:
            with open(self.__file_path, 'r') as f:
                dictnew = json.loads(f.read())
                for key, value in dictnew.items():
                    self.__objects[key] = self.classes[
                        value["__class__"]](**value)
        except FileNotFoundError:
            pass
