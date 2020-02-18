#!/usr/bin/python3
"""
Define: FileStorage Class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an File Storage.

    Attributes:
        __file_path (str): Json file path.
        __Objects (dict): Dict of saved Objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retreive all class instances objects
        Arguments:
            None
        Retruns:
            (list): all created objects list
        """
        return FileStorage.__objects

    def new(self, obj):
        """Create new Object
        Arguments:
            obj (class): object to create
        Returns:
            None
        """
        FileStorage.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Save new model
        Argumets:
            None
        Returns:
            None
        """
        to_store = {obj: FileStorage.__objects[obj].to_dict(
        ) for obj in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(to_store, f, indent=2)

    def reload(self):
        """Reload data from json file
        Arguments:
            None
        Returns:
            None
        """
        try:
            with open(FileStorage.__file_path) as f:
                data = json.load(f)
                for i in data.values():
                    cl_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cl_name)(**i))
        except Exception:
            pass
