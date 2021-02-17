#!/usr/bin/python3
"""
definition of FileStorage class
"""

import json
from ..base_model import BaseModel
from ..user import User
from ..place import Place
from ..city import City
from ..amenity import Amenity
from ..review import Review
from ..state import State


class FileStorage():
    """
    FileStorage
    class that manage the storage
    of the project's objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        all
        public instance method that
        return a dict with a key and a value
        the value are the objects of the
        program.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        new
        public instance method that
        create a new key-value for the
        storage.

        Arguments
            obj = the object to add.
        """
        FileStorage.__objects["{}.{}".format(type(obj).__name__,
                                             obj.id)] = (obj)

    def save(self):
        """
        save
        public instance method that
        save the dictionary to a json
        file.
        """

        diccionario = {}
        for obj_id in FileStorage.__objects.keys():
            obj = FileStorage.__objects[obj_id]
            diccionario[obj_id] = obj.to_dict()

        with open(FileStorage.__file_path, mode="w",
                  encoding="UTF8") as textfile:
            dict1 = json.dumps(diccionario)
            textfile.write(dict1)

    def reload(self):
        """
        reload
        public instance method that
        reload the list of objects of the project.
        """

        try:
            with open(FileStorage.__file_path, mode="r",
                      encoding="UTF8") as textfile:
                jsonstr = textfile.read()
                lsdicts = json.loads(jsonstr)

            for obj_id in lsdicts.keys():
                obj = lsdicts[obj_id]
                listkey = obj_id.split(".")
                classname = listkey[0]
                a = eval(classname)(**obj)
                FileStorage.__objects[obj_id] = (a)
        except Exception:
            pass
