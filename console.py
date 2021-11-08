#!/usr/bin/python3
"""
Console
"""
import cmd
import shlex
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """Console"""
    prompt = '(hbnb) '

    classes = {
        "BaseModel": BaseModel
    }

    def do_EOF(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """ Overrides the emptyline method of CMD
        """
        pass

    def do_create(self, args):
        """Create id for object"""
        args = args.split(' ')
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        insta = BaseModel()
        print(insta.id)
        models.storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance\n
        """
        token = shlex.split(arg)
        if len(token) == 0:
            print("** class name missing **")

        elif token[0] not in self.classes:
            print("** class doesn't exist **")

        elif len(token) == 1:
            print("** instance id missing **")

        else:
            ins = models.storage.all()
            key = token[0] + "." + token[1]
            if key in ins:
                print(ins[key])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
