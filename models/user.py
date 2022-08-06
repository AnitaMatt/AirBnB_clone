#!/usr/bin/python3
"""The class user"""

from models.base_model import BaseModel


class User(BaseModel):
    """Attribute User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
