#!/usr/bin/python3
"""this class serializes instances to a JSON file
 and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """this class is storing files"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        new_json = {}

        for key in self.__objects:
            new_json[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(new_json, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist
        no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                for key, value in json.load(file).items():
                    attr_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attr_value
        except FileNotFoundError:
            pass
