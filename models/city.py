#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationships
from os import getenv

class City(BaseModel, Base if (getenv("HBNB_TYPE_STORAGE")=="db") else object):
    """ The city class, contains state ID and name """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__= "cities"
        name = Column(String(128), nullable = False)
        state_id = Column(String(60), nullable = False, ForeignKey = "states.id")
        places = relationships("Place",
                                backref="cities", 
                                cascade= "all, delete",
                                passive_delete=True)
    else:
        state_id = ""
        name= ""

