#!/usr/bin/python3

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State

class FileStorage():
    """File Storage Class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """All Instances"""
        # class_name = self.__class__.__name__
        return FileStorage.__objects
    
    
    def new(self, obj):
        """New instances"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
    

    def save(self):
        """Save Instances"""
        data = {}
        for k, v in FileStorage.__objects.items():
            data[k] = v.to_dict()
        
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def reload(self):
        """Realoads Instances"""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                json_dict = json.loads(file.read())           
                for k, v in json_dict.items():
                    self.__objects[k] = eval(v['__class__'])(**v)

