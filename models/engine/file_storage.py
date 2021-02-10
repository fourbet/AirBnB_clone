#!/usr/bin/python3
"""
File Storage module
Serializes instances to a JSON file and
deserializes JSON file to instances
"""
import json
from os import path

from models.base_model import BaseModel

class FileStorage():
    """ FileStorage class

    Private calss attributes:
        __file_path (str): path to the JSON file
        __objects (dict): store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """  Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        with open(self.__file_path, mode='w+', encoding='utf-8') as f:
             my_dict = {k: v.to_dict() for k, v in self.__objects.items()}
             json.dump(my_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        if path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                my_dict = json.load(f)
                for k, v in my_dict.items():
                    cls = v["__class__"]
                    self.new(eval(cls)(**v))
