#!/usr/bin/python3

import json
from ..base_model import BaseModel

class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = (obj)

    def save(self):

        diccionario = {}
        for obj_id in FileStorage.__objects.keys():
            obj = FileStorage.__objects[obj_id]
            diccionario[obj_id] = obj.to_dict()

        with open(FileStorage.__file_path, mode="w", encoding="UTF8") as textfile:
            dict1 = json.dumps(diccionario)
            textfile.write(dict1)

    def reload(self):

        try:
            with open(FileStorage.__file_path, mode="r", encoding="UTF8") as textfile:
                jsonstr = textfile.read()
                lsdicts = json.loads(jsonstr)

            for obj_id in lsdicts.keys():
                obj = lsdicts[obj_id]
                a = BaseModel(**obj)
                FileStorage.__objects[obj_id] = (a)
        except Exception:
            pass
