#!/usr/bin/python3
"""
Module console.py - a command-line interpreter for HBNB project
"""

import cmd
from datetime import datetime
import json
import shlex

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the HBNB project.
    """

    prompt = "(hbnb) "

    All_class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_EOF(self, arg):
        """
        Quit command. Allows the user to exit the program using CTRL+D.
        """
        print("")
        return True

    def do_quit(self, arg):
        """
        Quit command. Allows the user to exit the program by typing 'quit'.
        """
        return True

    def do_nothing(self, arg):
        """
        Dummy command that does nothing.
        """
        pass

    def emptyline(self):
        """
        Called when an empty line + ENTER is entered. It shouldn't execute anything.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
