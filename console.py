#!/usr/bin/python3
"""Define: HBnBCommand Class"""

import cmd
import json

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): Command line prompt.
        __classes_names: Models classes names
    """

    prompt = "(hbnb) "
    help_msg = "jekrhgkurehn"
    __classes_names = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        pass
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_show(self, arg):
        if  not len(arg):
            print("** class name missing **")
            return
        if arg not in HBNBCommand.__classes_names:
            print("** class doesn't exist **")
    
    def do_create(self, arg):
        if  not len(arg):
            print("** class name missing **")
            return
        if arg not in HBNBCommand.__classes_names:
            print("** class doesn't exist **")
        else:
            model = eval(arg)()
            print(model.id)
            storage.save()
            
    
    def do_update(self):
        pass

    def do_destroy(self):
        pass

    def do_all(self):
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()