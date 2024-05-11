#!/usr/bin/python3

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
