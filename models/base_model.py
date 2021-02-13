#!/usr/bin/python3

import uuid
from datetime import datetime

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
            d = datetime.now()
            self.created_at = d.isoformat()
            self.updated_at = d.isoformat()

    def save(self):
        u = datetime.now()
        self.updated_at = u.isoformat()

    def to_dict(self):
        self.__dict__['__class__'] = type(self).__name__
        return self.__dict__

    def __str__(self):
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))