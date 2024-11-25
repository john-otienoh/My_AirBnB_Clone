import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
import models

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if len(arg) > 0:
            lines = arg.split()
            if len(lines) > 0:
                if lines[0] == "BaseModel":
                    obj = BaseModel()
                    obj.save()
                    print(obj.id)
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")
    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        classes_list = [
            "BaseModel", "User", "state", "City", 
            "Amenity", "Place", "Review"
        ]
        if len(arg) > 0:
            lines = arg.split()
            if len(lines) > 0:
                class_name = lines[0]
                if class_name in classes_list:
                    if len(lines) > 1:
                        data_dict = models.storage.all()
                        query = f"{class_name}.{lines[1]}"
                        if query in data_dict:
                            print(data_dict[query])
                        else:
                            print("*** no instance found ***")
                    else:
                        print("*** instance id missing ***")

                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")
    
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        classes_list = [
            "BaseModel", "User", "state", "City", 
            "Amenity", "Place", "Review"
        ]
        if len(arg) > 0:
            lines = arg.split()
            if len(lines) > 0:
                class_name = lines[0]
                if class_name in classes_list:
                    if len(lines) > 1:
                        data_dict = models.storage.all()
                        query = f"{class_name}.{lines[1]}"
                        if query in data_dict:
                            del (data_dict[query])
                            print(f"Deleting user id {query}")
                            models.storage.save()
                        else:
                            print("*** no instance found ***")
                    else:
                        print("*** instance id missing ***")

                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")


    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        classes_list = [
            "BaseModel", "User", "state", "City", 
            "Amenity", "Place", "Review"
        ]
        if len(arg) > 0:
            lines = arg.split()
            if len(lines) > 0:
                class_name = lines[0]
                if class_name in classes_list:
                    instance_list = []
                    for k,v in models.storage.all().items():
                        if class_name in k:
                            instance_list.append(str(v))
                    print(instance_list)
                else:
                    print("*** Class doesn't exist ***")
        else:
            instance_list = []
            for k,v in models.storage.all().items():
                instance_list.append(str(v))         
            print(instance_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id 
        by adding or updating attribute (save the change into the JSON file).
        """
        classes_list = [
            "BaseModel", "User", "state", "City", 
            "Amenity", "Place", "Review"
        ]
        attr_list = ["id", "created_at", "updated_at"]
        if len(arg) > 0:
            lines = arg.split()
            if len(lines) > 0:
                class_name = lines[0]
                if class_name in classes_list:
                    if len(lines) > 1:
                        data_dict = models.storage.all()
                        query = f"{class_name}.{lines[1]}"
                        if query in data_dict:
                            if len(lines) > 2:
                                if len(lines) > 3:
                                    if lines[3] not in attr_list:
                                        setattr(data_dict[query], str(lines[2]), str(lines[3]))
                                else:
                                    print("*** value missing ***")
                            else:
                                print("*** attribute name missing ***")   
                        else:
                            print("*** no instance found ***")
                    else:
                        print("*** instance id missing ***")

                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
