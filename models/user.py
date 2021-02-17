#!/usr/bin/python3
"""
definition of class User
"""

from .base_model import BaseModel
import models


class User(BaseModel):
    """
    User
    class that define a user
    in the project.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
