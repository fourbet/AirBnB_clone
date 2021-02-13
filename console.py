#!/usr/bin/python3
"""
Entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Amenity",
               "Place", "Review"]
    errors = {
        "ClassMissing": "** class name missing **",
        "ClassUnknown": "** class doesn't exist **",
        "IdMissing": "** instance id missing **",
        "IdUnknown": "** no instance found **",
        "AttrMissing": "** attribute name missing **",
        "ValueMissing": "** value missing **"
    }

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
            return (print(self.errors["ClassMissing"]))
        if cls not in self.classes:
            return (print(self.errors["ClassUnknown"]))

        instance = globals()[cls]
        new = instance()
        new.save()
        print(new.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        cmd = line.split()
        if not cmd:
            return (print(self.errors["ClassMissing"]))
        if cmd[0] not in self.classes:
            return (print(self.errors["ClassUnknown"]))
        if len(cmd) == 1:
            return (print(self.errors["IdMissing"]))
        all_objs = storage.all()
        search_id = "{}.{}".format(cmd[0], cmd[1])
        for obj_id in all_objs.keys():
            if search_id == obj_id:
                return (print(all_objs[obj_id]))
        return (print(self.errors["IdUnknown"]))

    def do_all(self, cls):
        """Prints all string representation of all instances based
        or not on the class name"""
        if cls and cls not in self.classes:
            return (print(self.errors["ClassUnknown"]))
        all_objs = storage.all()
        arr_objs = []
        for obj_id in all_objs.keys():
            arr_objs.append(all_objs[obj_id].__str__())
        print(arr_objs)

    def do_destroy(self, line):
        "Deletes an instance based on class name or id"
        cmd = line.split()
        if not cmd:
            return(print(self.errors["ClassMissing"]))
        if len(cmd) < 2:
            return(print(self.errors["IdMissing"]))
        if cmd[0] not in self.classes:
            return(print(self.errors["ClassUnknown"]))
        else:
            try:
                k = cmd[0] + '.' + cmd[1]
                if k in storage.all():
                    del storage.all()[k]
                    storage.save()
                else:
                    print(self.errors["IdUnknown"])
            except Exception as e:
                print(self.errors["ClassUnknown"])

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        cmd = line.split()
        if not cmd:
            return(print(self.errors["ClassMissing"]))
        if cmd[0] not in self.classes:
            return(print(self.errors["ClassUnknown"]))
        if len(cmd) == 1:
            return(print(self.errors["IdMissing"]))
        k = cmd[0] + "." + cmd[1]
        if k not in storage.all().keys():
            return(print(self.errors["IdUnknown"]))
        if len(cmd) == 2:
            print(self.errors["AttrMissing"])
        elif len(cmd) == 3:
            print(self.errors["ValueMissing"])
        else:
            k = cmd[0] + '.' + cmd[1]
            val = cmd[3]
            try:
                if val.isdigit():
                    val = int(val)
                elif float(val):
                    val = float(val)
            except ValueError:
                pass
            if k in storage.all():
                setattr(storage.all()[k], cmd[2], cmd[3])
                storage.save()

    def emptyline(self):
        """empty line"""
        pass

    def default(self, line):
        """Method to take care of following commands:
        <class name>.all()
        <class name>.show(<id>)
        <class name>.destroy(<id>)
        <class name>.update(<id>, <attribute name>, <attribute value>)
        <class name>.update(<id>, <dictionary representation)
        """
        commands = {"all()": self.do_all,
                    "show()": self.do_show,
                    "destroy()": self.do_destroy,
                    "update()": self.do_update}

        if '.' in line:
            cmd = line.split(".")
            class_name = cmd[0]
            method_name = cmd[1]
            if class_name in self.classes and method_name in commands.keys():
                commands[method_name](class_name)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
