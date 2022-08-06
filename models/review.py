#!/usr/bin/python3
"""The review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Attribute review"""
    place_id = ""
    user_id = ""
    text = ""
