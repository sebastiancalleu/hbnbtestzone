#!/usr/bin/python3

import uuid
from datetime import datetime
import models

class BaseModel():

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key in kwargs:
                if key != "__class__" and key != "created_at" and key != "updated_at":
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
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        d = self.__dict__.copy()
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        d['__class__'] = type(self).__name__
        return d

    def __str__(self):
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))
