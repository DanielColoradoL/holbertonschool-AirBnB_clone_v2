#!/usr/bin/python3
"""This module defines a class to manage DB for hbnb clone"""
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State


class DBStorage():
    """This class manages DBStorage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates a new DBStorage"""
        if (environ['HBNB_ENV'] == "test"
           and self.__engine is not None):
            Base.metadata.drop_all(self.__engine)

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(
                                          environ["HBNB_MYSQL_USER"],
                                          environ["HBNB_MYSQL_PWD"],
                                          environ["HBNB_MYSQL_HOST"],
                                          environ["HBNB_MYSQL_DB"]
                                          ), pool_pre_ping=True)
        self.__session = sessionmaker(bind=self.__engine)

    def all(self, cls=None):
        """Select from the DB
        Based on the given class
        If no class is given, return everything"""
        output = {}
        classes = [State, City]
        if cls is None:
            for s_class in classes:
                query = self.__session.query(s_class).all()
                for object in query:
                    key = f"{type(object).__name__}.{object.id}"
                    output[key] = object
        else:
            query = self.__session.query(cls).all()
            for object in query:
                key = f"{type(object).__name__}.{object.id}"
                output[key] = object
        return output

    def new(self, obj):
        """Adds obj to the current session"""
        self.__session.add(obj)

    def save(self):
        """Save the session to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes and object from the current session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload everything with a thread safe session"""
        from models.city import City
        from models.state import State
        from models.user import User
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        b_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(b_session)
