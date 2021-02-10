#!/usr/bin/python3
"""
Serializes instances to a JSON file and deserializes JSON file to instances
"""


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
