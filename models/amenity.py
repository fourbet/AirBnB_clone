#!/usr/bin/python3
"""
The prototype for Amenity class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel

    Public class attributes:
        name (str): name
    """
    name = ""
