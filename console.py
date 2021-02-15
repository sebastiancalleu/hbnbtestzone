#!/usr/bin/python3
""" Console command interpreter hbnb. """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Console interpreter command."""

    prompt = '(hbnb) '

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


if __name__ == '__main__':

    import sys

    if len(sys.argv) > 1:
        """ Take arguments  """
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        """ cmdloop() is the main processing loop of the interpreter """
        HBNBCommand().cmdloop()