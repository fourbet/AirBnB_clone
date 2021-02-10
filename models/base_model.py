#!/usr/bin/python3
""" Defines all common attributes/methods for other classes """
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ BaseModel Class """

    def __init__(self):
        """ Constructor of BaseModel """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """ Print """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at with the current datetime """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the instance """
        my_dict = dict(self.__dict__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = type(self).__name__
        return my_dict
