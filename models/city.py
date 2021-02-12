#!/usr/bin/python3
"""
The prototype for City class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherits from BaseModel

    Public class attributes:
        state_id (str): state id
        name (str): city name
    """
    state_id = ""
    name = ""
