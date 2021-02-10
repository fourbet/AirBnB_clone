#!/usr/bin/python3
""" Defines all common attributes/methods for other classes """
from uuid import uuid4
from datetime import datetime as dt
from models import storage

class BaseModel():
    """ BaseModel Class """

    def __init__(self, *args, **kwargs):
        """ Constructor of BaseModel """

        if kwargs:
            for k, v in kwargs.items():
                if k in ("created_at", "updated_at"):
                    setattr(self, k, dt.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                elif k[0] != '_':
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = dt.utcnow()
            self.updated_at = dt.utcnow()
            storage.new(self)

    def __str__(self):
        """ Print """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at with the current datetime """
        self.updated_at = dt.utcnow()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the instance """
        my_dict = dict(self.__dict__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = type(self).__name__
        return my_dict
