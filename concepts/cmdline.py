#!/usr/bin/python3
import cmd

class CmdLine(cmd.Cmd):
    """Custom Command Line Program"""
    intro = '''Welcome to Outis CmdLine Program.
    ******Type help or ? to list commands.*******\n'''
    prompt = '(outisCmd) '

    def do_great(self, arg):
        """Greets the user."""
        print(f"Hello {arg}!")

    def do_list(self, arg):
        """Lists all avaialble commands."""
        print("Available commands: greet, exit, list")

    def do_exit(self, arg):
        """Exits the application."""
        print('Thank you for using Outis CmdLine')
        return True
    
    def default(self, line):
        """Method called on an input line when the command prefix is not recognized."""
        print(f"Unrecognized Command {line}")

if __name__ == "__main__":
    CmdLine().cmdloop()
