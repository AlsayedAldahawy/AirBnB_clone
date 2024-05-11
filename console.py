#!/usr/bin/python3

"""
console.py module contains the entry point of the command interpreter:
"""

import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class provides a command-line interface for an application.

    Attributes:
        prompt (str): The command prompt displayed to the user.

    Methods:
        do_quit(self, command):
            Handles the 'quit' command to exit the program.

        do_EOF(self, arg):
            Handles the end-of-file (EOF) condition to exit the program.

        help_quit(self):
            Prints the help documentation for the 'quit' command.
    """

    prompt = "(hbnb)"

    def do_quit(self, command):
        """
        Handles the 'quit' command to exit the program.
        """
        exit()

    def help_quit(self):
        """
        Prints the help documentation for the 'quit' command.
        """
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """
        Handles the end-of-file (EOF) condition to exit the program.
        """
        print()
        exit()

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        elif line == "BaseModel":
            obj = BaseModel()
            storage.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        print("Creates a new instance of BaseModel,\nsaves it\
              (to the JSON file) and prints the id.\nEx: $ create BaseModel")

    def do_show(self, arg):

        args = arg.split()
        storage.reload()

        list_of_ids = []

        for key in storage._FileStorage__objects:
            id = key.split(".")[1]
            list_of_ids.append(id)

        # print("LOIDs",list_of_ids)
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            # print(";;;" , storage._FileStorage__objects )
            if args[1] not in list_of_ids:
                print("** no instance found **")
            else:
                print(storage._FileStorage__objects["BaseModel." + args[1]])

    def do_destroy(self, arg):
        args = arg.split()
        storage.reload()

        list_of_ids = []

        for key in storage._FileStorage__objects:
            id = key.split(".")[1]
            list_of_ids.append(id)

        # print("LOIDs",list_of_ids)
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            # print(";;;" , storage._FileStorage__objects )
            for id in args[1:]:
                if id not in list_of_ids:
                    print("** no instance found **")
                else:
                    try:
                        del storage._FileStorage__objects["BaseModel." + id]
                    except Exception:
                        pass

        storage.save()

    def do_all(self, arg):
        args = arg.split()

        if not arg or args[0] in ("BaseModel"):
            storage.reload()

            list_of_dicts = []
            list_of_dicts = [str(value)
                             for value in
                             storage._FileStorage__objects.values()]
            print(list_of_dicts)

        else:
            print("** class doesn't exist **")

    def do_update(self, arg):

        args = arg.split()
        storage.reload()

        list_of_ids = []

        for key in storage._FileStorage__objects:
            id = key.split(".")[1]
            list_of_ids.append(id)

        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[1] not in list_of_ids:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj = storage._FileStorage__objects["BaseModel." + args[1]]
            try:
                setattr(obj, args[2], args[3])
            except Exception:
                print("Unacceptable attribute name")

        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
