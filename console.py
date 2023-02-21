#!/usr/bin/env python3
"""program called console.py that contains
the entry point of the command interpreter"""
import cmd

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class HBNBCommand(cmd.Cmd):
    """program called console.py that contains
    the entry point of the command interpreter"""

    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_quit(self, arg):
        """exit thr program"""
        print("bay bay -From Rayane")
        return True

    def do_EOF(self, arg):
        """exit thr program with EOF """
        print()
        return True

    def do_create(self, arg):
        """create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based"""
#       args = arg.split()
 #       if not arg:
  #           print("** class name missing **")
 #        elif arg != "BaseModel":
#            print("** class doesn't exist **")
#        elif len(args) < 2:
 #           print("** instance id missing **")
  #      elif len(args) == 3:
   #         args != "BaseModel"
    #        print("** no instance found **")
   #     else:
  #          obj = HBNBCommand()
 #           print(repr(obj))
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")

        args = arg.split()
        if len(args) == 1:
            print("** instance id missing **")

        class_name = args[0]
        instance_id = args[1]
        key = class_name + "." + instance_id

        if key not in models.storage.all():
            print("** no instance found **")

        instance = models.storage.all()[key]
        print(instance)

    def do_destroy(self, arg):
#        args = arg.split()
#        if not arg:
#            print("** class name missing **") 
#        elif arg != "BaseModel":
#            print("** class doesn't exist **")
#        elif len(args) < 2:
#            print("** instance id missing **")
        #else:
            #del
        if not arg:
            print("** class name missing **")
        args = arg.split()
        if arg not in HBNBCommand:
            print("** class doesn't exist **")

        if len(args) == 1:
            print("** instance id missing **")

        class_name = args[0]
        instance_id = args[1]
        key = class_name + "." + instance_id

        if key not in models.storage.all():
            print("** no instance found **")
            return

        all_file = models.storage.all()[key]
        del all_file
        models.storage.save()
    def do_all(self, arg):
        if arg not in models.classes.keys():
            print("** class doesn't exist **")


    def do_update(self, args):
        """ Updates an instance based on the class name
        and id by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = args.split()

        if len(args) == 0:
            print("** class name missing **")

        #if args[0] not in BaseModel:
         #   print("** class doesn't exist **")

        if len(args) == 1:
            print("** instance id missing **")

        if len(args) == 2:
            print("** attribute name missing **")

        if len(args) == 3:
            print("** value missing **")


    

    def do_help_quit(self, arg):
        """help to qiut """
        print("Quit command to exit the program")

    def do_help_EOF(self, arg):
        """help to EOF"""
        print("EOF command to exit the program")

    def do_help_create(self, arg):
        """help to create"""
        print("""'create' command creates an instant of BaseModel if you add
              class as argument after it""")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
