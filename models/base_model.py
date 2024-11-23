#!/usr/bin/python3
"""
models/base_model.py
BaseModel class
"""
import uuid
from datetime import datetime
import models

class BaseModel():
    """class that defines all common attributes/methods for other classes:"""
    def __init__(self, *arg, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, k, v)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())

            if 'created_at' not in kwargs:
                self.created_at = datetime.now()

            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
    
    def save(self):
        """Updates 'updated_at' attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
        
    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance:"""
        result = self.__dict__.copy()
        result['__class__' ] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()

        return result
    
    def __str__(self):
        """Returns the string representation of the class."""
        class_name = self.__class__.__name__
        return f"{[class_name]} ({self.id}) {self.__dict__}"
    