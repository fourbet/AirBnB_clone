#!/usr/bin/python3
"""
The prototype for State Class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State Class that inherits from BaseModel

    Public class attributes:
        name (str): state name'
    """
    name = ""
