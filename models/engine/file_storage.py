#!/usr/bin/python3
"""
Serializes instances to a JSON file and deserializes JSON file to instances
"""
import json


class FileStorage():
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all method """
        return self.__objects

    def new(self, obj):
        """ new method """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """ save method """
        my_dict = {k: v.to_dict() for k, v in self.__objects.items()}

        with open(self.__file_path, mode='w+', encoding='utf-8') as f:
            json.dump(my_dict, f)

    def reload(self):
        """ reload method """
        my_dict = {}
        try:
            from models.base_model import BaseModel
            with open(self.__file_path) as f:
                my_dict = json.load(f)
                for k, v in my_dict.items():
                    self.__objects[k] = BaseModel(**v)
        except:
            pass
