#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity

storage_type = os.getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column('place_id',
               String(60),
               ForeignKey('places.id'),
               nullable=False),
        Column('amenity_id',
               String(60),
               ForeignKey('amenities.id'),
               nullable=False)
    )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if storage_type == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship("Review", back_populates="place",
                               cascade="delete, delete-orphan")
        amenities = relationship("Amenity", secondary='place_amenity',
                                 viewonly=False,
                                 overlaps="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Retrives reviews objects
            where place_id match """
            from models import storage
            list_of_reviews = storage.all(Review)
            return [review for review in list_of_reviews.values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            return [Amenity(id=amenity_id) for amenity_id in self.amenity_ids]

        @amenities.setter
        def amenities(self, amenity):
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
