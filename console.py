#!/usr/bin/python3
"""Define: HBnBCommand Class"""

import cmd
import json
import re
from shlex import split

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
        __classes_names (dict): Models classes names
        __types (dict): Allowed types
    """

    prompt = "(hbnb) "
    __types = {str, int, float}
    __classes_names = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    @staticmethod
    def arg_parser(line):
        """Command line arguments parser
        Arguments:
            line (str): arguments string format
        Returns:
            (list)
        """
        match = re.search(r"\{(.*?)\}", line)
        if match is None:
            return [i.strip(",") for i in split(line)]
        else:
            argl = [i.strip(",") for i in split(line[:match.span()[0]])]
            return argl.append(match.group())

    def default(self, arg):
        """When Invalid syntax typed"""
        __methods = {
            "all": self.do_all,
            "count": self.do_count,
            "update": self.do_update,
            "destroy": self.do_destroy,
            "show": self.do_show
        }
        cmd = {
            "model": "",
            "method": "",
            "arg": ""
        }
        match = re.search(r"\.", arg)
        if match is not None:
            cmd["model"] = arg[:match.span()[0]]
            cmd["method"] = arg[match.span()[1]:]
            match = re.search(r"\((.*?)\)", cmd["method"])
            if match is not None:
                cmd["method"] = cmd["method"][:match.span()[0]]
                cmd["arg"] = match.group()[1:-1]
                if cmd["method"] in __methods.keys():
                    line = "{} {}".format(cmd["model"], cmd["arg"])
                    return __methods[cmd["method"]](line)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def emptyline(self):
        """Nothing to do when an empty line typed"""
        pass

    def do_quit(self, arg):
        """Quit command to quit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_show(self, arg):
        """Display string representation of a class with id
        Usage: show <class> <id>
        """
        arg_list = self.arg_parser(arg)
        if not len(arg_list):
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__classes_names:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        data = storage.all()
        key = "{}.{}".format(arg_list[0], arg_list[1])
        if key not in data.keys():
            print("** no instance found **")
            return False
        print(data[key])

    def do_create(self, arg):
        """
        Create a new class instance and display its <id>.
        Usage: create <class>
        """
        arg_list = self.arg_parser(arg)
        if not len(arg_list):
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__classes_names:
            print("** class doesn't exist **")
            return False
        model = eval(arg_list[0])()
        print(model.id)
        storage.save()

    def do_update(self, arg):
        """Update specefic attribute of a class instance of a given <id>
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        arg_list = self.arg_parser(arg)
        if not len(arg_list):
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__classes_names:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        data = storage.all()
        key = "{}.{}".format(arg_list[0], arg_list[1])
        if key not in data.keys():
            print("** no instance found **")
            return False
        obj = data[key]
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            if type(eval(arg_list[2])) == dict:
                for k, v in eval(arg_list[2]).items():
                    if (k in obj.__class__.__dict__.keys() and
                            type(obj.__class__.__dict__[k]) in self.__types):
                        obj.__dict__[k] = type(obj.__class__.__dict__[k])(v)
                    else:
                        obj.__dict__[k] = v
                storage.save()
                return False
            print("** value name missing **")
            return False

        if arg_list[2] in obj.__class__.__dict__.keys():
            obj.__dict__[arg_list[2]] = type(
                obj.__class__.__dict__[arg_list[2]])(arg_list[3])
        else:
            obj.__dict__[arg_list[2]] = (arg_list[3])
        storage.save()

    def do_destroy(self, arg):
        """Delete a class instance of a given <id>
        Usage: destroy <class>
        """
        arg_list = self.arg_parser(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__classes_names:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        data = storage.all()
        key = "{}.{}".format(arg_list[0], arg_list[1])
        if key not in data.keys():
            print("** no instance found **")
            return False
        del data[key]
        storage.save()

    def do_count(self, arg):
        """get the number of instances of a given class
        Usage: count <class>
        """
        arg_list = self.arg_parser(arg)
        data = storage.all().values()
        count = 0
        for obj in data:
            if arg_list[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_all(self, arg):
        """Display string representation of all instances of a given class
        or all instances objects.
        Usage: all or all <class>
        """
        arg_list = self.arg_parser(arg)
        data = storage.all()
        model_data = []
        if not len(arg_list):
            for obj in data.values():
                model_data.append(obj.__str__())
        else:
            if arg_list[0] not in HBNBCommand.__classes_names:
                print("** class doesn't exist **")
                return False
            for obj in data.values():
                if arg_list[0] == obj.__class__.__name__:
                    model_data.append(obj.__str__())
        print(model_data)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
