#!/usr/bin/python3
"""The city class"""

import models
from models.base_model import BaseModel


class City(BaseModel):
    """Attribute city"""
    state_id = ""
    name = ""
