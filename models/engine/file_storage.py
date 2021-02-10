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
        my_dict = {k: v.to_dict() for k,v in self.__objects.items()}
        
        with open(self.__file_path, mode='w+', encoding='utf-8') as f:
            json.dump(my_dict, f)

    def reload(self):
        """ reload method """
        try:
            with open(self.__file_path) as f:
                self.__objects = json.load(f)
        except:
            pass
