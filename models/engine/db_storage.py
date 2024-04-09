#!/usr/bin/python3
"""New engine DBStorage"""
import json
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

all_classes = {'State': State, 'City': City, 'User': User,
               'Place': Place, 'Review': Review, 'Amenity': Amenity}


class DBStorage:
    """Save in the database
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage instance"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """"manage dict all cls and entities"""
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))()
        obj_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f'{type(obj).__name__}.{obj.id}'
                obj_dict[key] = obj
        else:
            # Import these classes at the top
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = f'{cls.__name__}.{obj.id}'
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """
        Call remove() method on the private session attribute
        """
        self.__session.close()