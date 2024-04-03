#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    """Using DB"""
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    """Using FileStorage"""
    @property
    def cities(self):
        """Retrives City objects
        where id match """
        from models import storage
        list_of_cities = storage.all(City)
        return [city for city in list_of_cities.values()
                if city.state_id == self.id]
