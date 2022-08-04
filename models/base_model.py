#!/usr/bin/python3
""" BaseModel that defines all common sattribute for other classes"""
import uuid
from datetime import datetime


class BaseModel:
    """Base class for all other models"""
    def __init__(self):
        """initializing the base class and others to follow"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string method"""
        class_name = self.__class__.__name__
        return "[{}] ({}) <{}>".format(class_name, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        copy_dict = self.__dict__.copy()
        copy_dict["created_at"] = self.created_at.isoformat()
        copy_dict["updated_at"] = self.updated_at.isoformat()
        copy_dict["__class__"] = self.__class__.__name__
        return copy_dict
