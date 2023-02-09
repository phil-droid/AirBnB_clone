#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""User Module
This Module inherits from BaseModel class.
User Module contains the user information.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User Class
    Attributes:
        email (str): The User email
        password (str): The User password
        first_name (str): The user's first name
        last_name (str): The user's last name
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
