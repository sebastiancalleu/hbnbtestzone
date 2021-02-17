#!/usr/bin/python3
""" Console command interpreter hbnb. """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.state import State
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """ Console interpreter command."""

    prompt = '(hbnb) '
    listclasses = ["BaseModel", "User", "Place",
                   "Review", "City", "State", "Amenity"]

    def do_quit(self, argv):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, argv):
        """EOF command to exit the program
        """
        return print(), True

    def emptyline(self):
        """An empty line + ENTER only print a new line. """
        pass

    def do_create(self, classtr):
        """
        do_create
        Command to create an object

        Usage: create <classname>

        Arguments
            classtr = <classname> the name of the
            class of the object we want to create.

        Return
            Object and print the id of the object.
        """
        if classtr:
            if classtr in HBNBCommand.listclasses:
                obj = eval(classtr)()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, str1):
        """
        do_show
        Command to show a object string representation

        Usage: show <classname> <object id>

        Arguments
            str1 = string that contain classname and object id.

        Return
            print the object string representation.
        """
        if str1:
            list2 = str1.split()
            if list2[0] in HBNBCommand.listclasses:
                if len(list2) == 2:
                    str2 = list2[0] + "." + list2[1]
                    dict1 = storage.all()
                    try:
                        print(dict1[str2])
                    except BaseException:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, str1):
        """
        do_destroy
        Command to destroy an object

        Usage: destroy <classname> <object id>

        Arguments
            str1 = string that contains the class name an object id.

        Return
            destroy the object and print nothing.
        """
        if str1:
            list2 = str1.split()
            if list2[0] in HBNBCommand.listclasses:
                if len(list2) == 2:
                    str2 = list2[0] + "." + list2[1]
                    dict1 = storage.all()
                    try:
                        del dict1[str2]
                        storage.save()
                    except BaseException:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, str1):
        """
        do_all
        Command to print objects (all or a class objects)

        Usage: all <classname>
               all

        Arguments
            str1 = string that contains classname.

        Return
            print the objects.
        """

        if str1 in HBNBCommand.listclasses or bool(str1) is False:
            dict1 = storage.all()
            list1 = []
            for obkey in dict1.keys():
                obj = dict1[obkey]
                if bool(str1) is True:
                    if str1 in obkey.split("."):
                        list1.append(str(obj))
                else:
                    list1.append(str(obj))
            if len(list1) == 0:
                pass
            else:
                print(list1)
        else:
            print("** class doesn't exist **")

    def do_update(self, str1):
        """
        do_update
        Command to update an attribute of a object

        Usage: update <classname> <object id>
        <attribute name> <attribute value>

        Arguments
            str1 = string that contains all
            the information to update the object.

        Return
            modifies the object and print nothing.
        """

        if str1:
            lexobj = shlex.split(str1)
            list2 = []
            for tokens in lexobj:
                list2.append(tokens.replace("\'", ""))
            if list2[0] in HBNBCommand.listclasses:
                if len(list2) == 4:
                    str2 = list2[0] + "." + list2[1]
                    dict1 = storage.all()
                    try:
                        obj = dict1[str2]
                        try:
                            atr = int(list2[3])
                        except:
                            try:
                                atr = float(list2[3])
                            except:
                                atr = list2[3].replace("\"", "")
                        setattr(obj, list2[2], atr)
                        obj.save()
                    except BaseException:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':

    import sys

    if len(sys.argv) > 1:
        """ Take arguments  """
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        """ cmdloop() is the main processing loop of the interpreter """
        HBNBCommand().cmdloop()
