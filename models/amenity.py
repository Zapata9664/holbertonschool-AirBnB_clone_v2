#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class Amenity(BaseModel, Base if (getenv("HBNB_TYPE_STORAGE")=="db")else object):
    """This class is the representation of amenities at a place"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place",
            secondary="place_amenity")
    else:
        name = ""
