#!/usr/bin/python3
"""serializes and deserializes JSON"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """File Storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary with all objects"""
        return self.__objects

    def new(self, obj):
        """add new object to dictionary"""
        name = obj.__class__.__name__ + "." + obj.id
        self.__objects[name] = obj

    def save(self):
        """save dictionary to file in JSON format"""
        dic = {}
        for k, v in self.__objects.items():
            dic[k] = v.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dic, f)

    def reload(self):
        """load JSON back into dictionary of objects"""
        try:
            with open(self.__file_path, "r") as f:
                dic = json.load(f)
            for k, v in dic.items():
                self.__objects[k] = eval(v["__class__"])(**v)
        except:
            pass
