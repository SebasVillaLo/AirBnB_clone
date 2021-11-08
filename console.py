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

    def do_show(sel, args):
        """Show the id of any object"""
        args = args.split(' ')

        if args[0] == 0:
            print("** class name missing **")
            return
        if args[0] in HBNBCommand.classes:
            if len(args) > 1:
                aux = models.storage.all()
                key = args[0] + '.' + args[1]
                if key in aux:
                    print(key[aux])
                    return
                else:
                    print("** no instance found **")
                    return
            else:
                print("** instance id missing **")
                return
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
