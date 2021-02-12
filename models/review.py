#!/usr/bin/python3

"""
The prototype for Review class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel

    Public class attributes:
        place_id (str)
        user_id (str)
        text (str))
"""
    place_id = ""
    user_id = ""
    text = ""
