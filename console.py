#!/usr/bin/python3
"""
Entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def do_create(self, cls):
        """ Creates a new instance of BaseModel"""
        if not cls:
            return (print("** class name missing **"))
        if cls != 'BaseModel':
            print("** class doesn't exist **")

        new = BaseModel()
        new.save()
        print(new.id)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
