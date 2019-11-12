#!/usr/bin/python3
""" Command interpreter for AirBNB clone """
import cmd
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """ CMD class for command interpreter """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file) and prints id
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        try:
            eval(arg)
        except:
            print("** class doesn't exist **")
            return

        new = eval(arg)()
        new.save()
        print(new.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance:
        based on the class name and id
        """
        splt = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if len(splt) == 1:
            print("** instance id missing **")
            return
        try:
            eval(splt[0])
        except:
            print("** class doesn't exist **")
            return
        name = splt[0] + "." + splt[1]
        dic = models.storage.all()
        if name not in dic.keys():
            print("** no instance found **")
            return
        print(dic[name])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        splt = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if len(splt) == 1:
            print("** instance id missing **")
            return
        try:
            eval(splt[0])
        except:
            print("** class doesn't exist **")
            return

        name = splt[0] + "." + splt[1]
        dic = models.storage.all()
        if name not in dic.keys():
            print("** no instance found **")
            return
        del dic[name]
        eval(splt[0])._count -= 1
        models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based on class name
        """
        new = []
        dic = models.storage.all()
        if len(arg) == 0:
            for k, v in dic.items():
                new.append(str(v))

        else:
            try:
                eval(arg)
            except:
                print("** class doesn't exist **")
                return

            for k, v in dic.items():
                name = k.split(".")
                if name[0] == arg:
                    new.append(str(v))
        print(new)

    def do_update(self, arg):
        """ Update or add attributes """
        splt = shlex.split(arg)
        if len(splt) == 0:
            print("** class name missing **")
            return
        try:
            eval(splt[0])
        except:
            print("** class doesn't exist **")
            return
        if len(splt) == 1:
            print("** instance id missing **")
            return
        if len(splt) == 2:
            print("** attribute name missing **")
            return
        if len(splt) == 3:
            print("** value missing **")
            return
        name = splt[0] + "." + splt[1]
        dic = models.storage.all()
        obj = dic[name]
        try:
            splt[3] = int(splt[3])
        except:
            try:
                splt[3] = float(splt[3])
            except:
                pass
        setattr(obj, splt[2], splt[3])
        obj.save()

    def default(self, arg):
        """ catches all functions that aren't defined """
        if len(arg) == 0:
            return
        splt = arg.split(".")

        if splt[1][:3] == "all":
            self.do_all(splt[0])

        elif splt[1][:5] == "count":
            print(eval(splt[0])._count)

        elif splt[1][:4] == "show":
            new_arg = splt[0] + " " + splt[1][5:-1]
            self.do_show(new_arg)

        elif splt[1][:7] == "destroy":
            new_arg = splt[0] + " " + splt[1][8:-1]
            self.do_destroy(new_arg)

        elif splt[1][:6] == "update":
            temp = (splt[0] + ',' + splt[1][7:-1]).split(",")
            if len(temp) == 4:
                new_arg = " ".join(temp)
                self.do_update(new_arg)
            if "{" in arg:
                on = 0
                new = """"""
                for x in arg:
                    if on == 1:
                        new += x
                    if x == "{":
                        new += x
                        on = 1
                    if x == "}":
                        break
                dic = eval(new)
                test = splt[1].split(",")
                for k, v in dic.items():
                    s = splt[0] + " " + test[0][7:] + " " + k + " " + str(v)
                    self.do_update(s)

    def emptyline(self):
        """ Handles empty line """
        pass

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        return True

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_help(self, arg):
        """ type help <topic> """
        cmd.Cmd.do_help(self, arg)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
