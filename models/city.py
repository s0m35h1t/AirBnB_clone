#!/usr/bin/python3
"""
Define: City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.

    Attributes:
        state_id (str): State id.
        name (str): City name.
    """

    state_id = ""
    name = ""
