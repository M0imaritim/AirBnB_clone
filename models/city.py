#!/usr/bin/python3
"""Defines city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """BaseModel child class"""
    state_id = ""
    name = ""
