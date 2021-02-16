#!/usr/bin/python3
""" a class review that inherits from BaseModel """
from .base_model import BaseModel


class Review(BaseModel):
    """ a class review that inherits from BaseModel """

    place_id = ''
    user_id = ''
    text = ''
