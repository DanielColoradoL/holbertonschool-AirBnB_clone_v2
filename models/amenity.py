#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship

storage_type = os.getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """Represents amenities a place can have"""
    __tablename__ = "amenities"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place",
                                       secondary='place_amenity',
                                       viewonly=False,
                                       back_populates="amenities")
    else:
        name = ""
