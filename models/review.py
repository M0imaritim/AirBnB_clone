#!/usr/bin/python3
"""Defines review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """BaseModel child class"""
    place_id = ""
    user_id = ""
    text = ""
