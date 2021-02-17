#!/usr/bin/python3
"""
definition of class BaseModel
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    BaseModel
    class that contain all the methods to define
    the objects.
    """

    def __init__(self, *args, **kwargs):
        """
        constructor
        define the initial attributes of each
        instance if is a new instance and use
        a dict to create a object from json

        Arguments
            kwargs = the dictionary to create the
            object.
        """
        if kwargs:
            for key in kwargs:
                if (key != "__class__" and key != "created_at" and
                        key != "updated_at"):
                    setattr(self, key, kwargs[key])
                if key == "created_at" or key == "updated_at":
                    d = datetime.strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, d)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        save
        public instance method that
        save the object to json throug
        filestorage.
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        to_dict
        public instance method that
        creates a dict with object
        attributes.
        """
        d = self.__dict__.copy()
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        d['__class__'] = type(self).__name__
        return d

    def __str__(self):
        """
        __str__
        method to change the string
        representation of the object.
        """
        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))
