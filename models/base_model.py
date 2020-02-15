#!/usr/bin/python3
"""
Define: BaseModel Class
"""
import uuid
from datetime import datetime
import models


time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)
        
    def __str__(self):
        """
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        """
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """
        """
        cl_dict = self.__dict__.copy()
        cl_dict["created_at"] = self.created_at.isoformat()
        cl_dict["updated_at"] = self.updated_at.isoformat()
        cl_dict["__class__"] = self.__class__.__name__
        return cl_dict
