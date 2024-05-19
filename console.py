#!/usr/bin/python3
import cmd
import json
import shlex
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from datetime import datetime

"""
Module consule.py a cmd console
"""


class HBNBCommand(cmd.Cmd):
    ''' a command interpreter class '''
    prompt = "(hbnb)"

    All_class_dict = {
        "BaseModel": BaseModel
    }

    def do_EOF(self, arg):
        '''Quit command CTRL+D to exit the program'''
        print("")
        return True

    def do_quit(self, arg):
        ''' Quit command to exit the program '''
        return True

    def do_nothing(self, arg):
        ''' does nothing '''
        pass

    def emptyline(self):
        ''' an empty line + ENTER shouldn’t execute anything '''
        pass

    def do_create(self, args):
        ''' Creates a new instance BaseModel, saves prints its id '''
        if args == "":
            print("** class name missing **")
            return
        arg = shlex.split(args)
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class doesn't exist **")
            return
        new = HBNBCommand.All_class_dict[arg[0]]()
        new.save()
        print(new.id)

    def do_show(self, args):
        ''' Prints the string repr of an instances class name and id '''
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        obj = storage.all()
        obj_key = arg[0] + "." + arg[1]
        if obj_key in obj:
            print(str(obj[obj_key]))
        else:
            print("** no instance found **")
