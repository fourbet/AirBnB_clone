#!/usr/bin/python3
"""
Entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models import storage

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
            return (print("** class doesn't exist **"))

        new = BaseModel()
        new.save()
        print(new.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        cmd = line.split()
        if not cmd:
            return (print("** class name missing **"))
        if cmd[0] != 'BaseModel':
            return (print("** class doesn't exist **"))
        if len(cmd) == 1:
            return (print("** instance id missing **"))
        all_objs = storage.all()
        search_id = "BaseModel.{}".format(cmd[1])
        for obj_id in all_objs.keys():
            if search_id == obj_id:
                return (print(all_objs[obj_id]))
        return (print("** no instance found **"))

    def do_all(self, cls):
        """Prints all string representation of all instances based
        or not on the class name"""
        if cls and cls != "BaseModel":
            return (print("** class doesn't exist **"))
        all_objs = storage.all()
        arr_objs = []
        for obj_id in all_objs.keys():
            arr_objs.append(all_objs[obj_id].__str__())
        print(arr_objs)

    def do_destroy(self, line):
        "Deletes an instance based on class name or id"
        cmd = line.split()
        if not cmd:
            print("** class name missing **")
            return
        elif len(cmd) < 2:
            print("** instance id missing **")
            return
        if cmd[0] not in classes:
            print("** class doesn't exist **")
            return
        for k, v in storage.all().items():
            if cmd[1] == v.id:
                del storage.all()[k]
                storage.save()
                return
        print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
