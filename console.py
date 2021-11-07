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
    prompt  = '(hbnb) '

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
        """Create"""
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()