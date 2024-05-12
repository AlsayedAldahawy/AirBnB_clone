#!/usr/bin/python3

"""
console.py module contains the entry point of the command interpreter:
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
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

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    prompt = "(hbnb)"

    def do_quit(self, command):
        """
        Handles the 'quit' command to exit the program.
        """
        exit()

    def do_EOF(self, arg):
        """
        Handles the end-of-file (EOF) condition to exit the program.
        """
        print()
        exit()

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of a specified class.

        Args:
            arg (str): The input argument containing the class name.

        Returns:
            None
        """

        args = arg.split()
        if not arg:
            print("** class name missing **")

        elif args[0]:
            for i in args[0:]:
                if i in HBNBCommand.classes:
                    obj = HBNBCommand.classes[i]()
                    storage.save()
                    print(obj.id)
                else:
                    print("** class doesn't exist **")
                    break

    def do_show(self, arg):
        """
        Displays information about a specific instance.

        Args:
        arg (str): The input argument containing class name and instance ID.

        Returns:
            None
        """
        args = arg.split()

        if check_args(arg):
            dict_lists_ids = dict_list_id()

            for id in args[1:]:
                if id not in dict_lists_ids[args[0]]:
                    print("** no instance found **")
                else:
                    print(storage._FileStorage__objects[args[0] + "."
                                                        + id])

    def do_destroy(self, arg):
        """
        Deletes an instance from the storage.

        Args:
        arg (str): The input argument containing class name and instance ID.

        Returns:
            None
        """
        args = arg.split()  # spliting the arguments line into a list of args

        if check_args(arg):
            dict_lists_ids = dict_list_id()

            for id in args[1:]:
                if id not in dict_lists_ids[args[0]]:
                    print("** no instance found **")
                else:
                    try:
                        del storage._FileStorage__objects[args[0] + "." + id]
                    except Exception:
                        pass
                storage.save()

    def do_all(self, arg):
        """
        Prints all instances or instances of a specific class.

        Args:
            arg (str): The input argument containing class name.

        Returns:
            None
        """

        args = arg.split()

        if not arg or args[0] in HBNBCommand.classes:
            storage.reload()
            list_of_dicts = []
            if not arg:
                list_of_dicts = [str(value)
                                 for value in
                                 storage._FileStorage__objects.values()]
            else:
                list_of_dicts = [str(value)
                                 for key, value in
                                 storage._FileStorage__objects.items()
                                 if key.split(".")[0] == args[0]]

            print(list_of_dicts)

        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an attribute of an instance.

        Args:
            arg (str): The input argument containing class name, instance ID,\
                attribute name, and value.

        Returns:
            None
        """
        args = arg.split()
        storage.reload()

        list_of_ids = []

        for key in storage._FileStorage__objects:
            id = key.split(".")[1]
            list_of_ids.append(id)

        if not arg:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.classes:
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
            obj = storage._FileStorage__objects[args[0] + "." + args[1]]
            try:
                setattr(obj, args[2], args[3])
            except Exception:
                print("Unacceptable attribute name")

        storage.save()

    # ----- ---- --- Help methods --- ---- -----

    def help_quit(self):
        """
        Prints the help documentation for the 'quit' command.
        """
        print("Quit command to exit the program\n")

    def help_create(self):
        print("Creates a new instance of BaseModel,\nsaves it\
            (to the JSON file) and prints the id.\nEx: $ create BaseModel")

    def help_show(self):
        print("show <class_name> <instance_id>: Display information\
              about an instance")

    def help_destroy(self):
        print(
            "destroy <class_name> <instance_1_id> ... <instance_N_id> : \
                Delete an instance")

    def help_all(self):
        print("all <class_name>: Print all instances or instances of a\
               specific class")

    def help_update(self):
        print("update <class_name> <instance_id> <attribute_name> <value>:\
               Update or add an attribute")


def dict_list_id():
    storage.reload()

    list_of_ids_bm = []  # list of BaseModel class ids
    list_of_ids_usr = []  # list of User class ids
    list_of_ids_sta = []
    list_of_ids_cit = []
    list_of_ids_amn = []
    list_of_ids_plc = []
    list_of_ids_rev = []
    dict_lists_ids = {}  # has two lists of ids for BaseModel, User

    for key in storage._FileStorage__objects:
        class_name = key.split(".")[0]
        id = key.split(".")[1]
        if class_name == "BaseModel":
            list_of_ids_bm.append(id)
        if class_name == "User":
            list_of_ids_usr.append(id)
        if class_name == "State":
            list_of_ids_sta.append(id)
        if class_name == "City":
            list_of_ids_cit.append(id)
        if class_name == "Amenity":
            list_of_ids_amn.append(id)
        if class_name == "Place":
            list_of_ids_plc.append(id)
        if class_name == "Review":
            list_of_ids_rev.append(id)

    dict_lists_ids["BaseModel"] = list_of_ids_bm
    dict_lists_ids["User"] = list_of_ids_usr
    dict_lists_ids["State"] = list_of_ids_sta
    dict_lists_ids["City"] = list_of_ids_cit
    dict_lists_ids["Amenity"] = list_of_ids_amn
    dict_lists_ids["Place"] = list_of_ids_plc
    dict_lists_ids["Review"] = list_of_ids_rev

    return dict_lists_ids


def check_args(arg):
    args = arg.split()
    if not arg:
        print("** class name missing **")
        return 0
    elif args[0] not in HBNBCommand.classes:
        print("** class doesn't exist **")
        return 0
    elif len(args) < 2:
        print("** instance id missing **")
        return 0
    return 1


if __name__ == '__main__':
    HBNBCommand().cmdloop()
