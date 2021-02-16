#!/usr/bin/python3

from .base_model import BaseModel
import models

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
