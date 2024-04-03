#!/usr/bin/python3
"""
This module defines a class to manage DB for hbnb clone
"""
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review


class DBStorage:
    """
    This class manages DBStorage of hbnb models
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Creates a link to the MySQL database
        """
        username = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        hostname = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(username, password, hostname,
                                              database), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage
        """
        output = {}
        classes = [State, City]
        if cls is None:
            for s_class in classes:
                query = self.__session.query(s_class).all()
                for obj in query:
                    key = f"{type(obj).__name__}.{obj.id}"
                    output[key] = obj
        else:
            query = self.__session.query(cls).all()
            for obj in query:
                key = f"{type(obj).__name__}.{obj.id}"
                output[key] = obj
        return output

    def new(self, obj):
        """
        Adds obj to the current session
        """
        self.__session.add(obj)

    def save(self):
        """
        Save the session to the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes and object from the current session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reload everything with a thread safe session
        """
        Base.metadata.create_all(self.__engine)
        b_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(b_session)
        self.__session = Session()

    def close(self):
        """
        Closes a session
        """
        self.__session.close()
