#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
    
    def save(self):
        """
        """
        to_store = {obj: FileStorage.__objects[obj].to_dict() for obj in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(to_store, f)
    
    def reload(self):
        """
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
