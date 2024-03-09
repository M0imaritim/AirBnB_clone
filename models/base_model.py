#!/usr/bin/python3
"""Defines the super class"""

import datetime
import uuid


class BaseModel:
    """This is the super class"""
    def __init__(self):
        """initializing attributes"""
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.datetime.now().isoformat()

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
