import cmd

class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter:"""
    intro = """
    *****Welcome to the AirBnB Console*****
        Type help or ? to list commands.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("Exiting the AirBnB program ...")
        return True
    
    def do_EOF(self, arg):
        """Exits the Application"""
        print("")
        return True
    
    def emptyline(self):
        """Override empty line behavior."""
        pass
    
    # def help(self, arg):
    #     if arg:
    #         try:
    #             print(self.help_commands[arg])
    #             print("")
    #         except KeyError:
    #             print(f"***No help on {arg} command!")
    #     else:
    #         print("Avaialble commands: ")
    #         for c in self.get_commands():
    #             print(f"    {c}")
    #         print("")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
