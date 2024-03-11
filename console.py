#!/usr/bin/python3

"""Defining the HBnB console"""

import cmd
import shlex
import models
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """console shell"""

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
