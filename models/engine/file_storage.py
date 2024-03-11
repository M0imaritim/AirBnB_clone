#!/usr/bin/python3
"""defines a file storage class"""

import json
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.user import User


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        dictn = {}
        for key, value in self.__objects.items():
            dictn[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        cl_dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                  'City': City, 'Amenity': Amenity, 'State': State,
                  'Review': Review}
        try:
            with open(self.__file_path, "r") as f:
                for key, value in json.load(f).items():
                    self.new(cl_dct[value['__class__']](**value))
        except FileNotFoundError:
            pass
