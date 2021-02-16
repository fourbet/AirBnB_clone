#!/usr/bin/python3
""" Defines all common attributes/methods for other classes """

from uuid import uuid4
from datetime import datetime as dt
import models


class BaseModel():
    """ BaseModel Class

    Public instance attributes:
        id (str): assign with an unique random id when created
        created_at (datetime): assign with the current datetime when created
        updated_at (datetime): assign with the current datetime when updated
    """

    def __init__(self, *args, **kwargs):
        """ Constructor of BaseModel

        Attributes:
            *args: unused
            **kwargs (dict)
        """

        if kwargs:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    setattr(self, k, dt.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                elif k != '__class__':
                    setattr(self, k, str(v))
        else:
            self.id = str(uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            models.storage.new(self)

    def __str__(self):
        """ Print """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        my_dict = dict(self.__dict__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = type(self).__name__
        return my_dict
