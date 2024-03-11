#!/usr/bin/python3
"""Defines the super class"""

import datetime
import uuid
from models import storage


class BaseModel:
    """This is the super class"""
    def __init__(self, *args, **kwargs):
        """initializing attributes"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = setattr(self, key, datetime.fromisoformat(value))
                if key != '__class__':
                    setattr(self, key, value)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now().isoformat()
        storage.save()

    def __str__(self):
        """prints name of class and its id"""
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
