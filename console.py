#!/usr/bin/python3

"""
console.py module contains the entry point of the command interpreter:
"""

import cmd
from models.base_model import BaseModel
from models import storage 


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
        print("Creates a new instance of BaseModel,\nsaves it (to the JSON file) and prints the id.\nEx: $ create BaseModel")

    def do_show(self, arg):

        args = arg.split()

        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            if args[1] not in storage._FileStorage__objects:
                print("** no instance found **")
            else:
                print(storage._FileStorage__objects[args[1]])

        
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
