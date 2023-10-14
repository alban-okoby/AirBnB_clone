#!/usr/bin/python3
"""
This module defines the FileStorage class, a storage engine for objects.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Represents an abstracted storage engine.

    Attributes:
        __file_path (str): The path to the JSON file for object storage.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary of all objects.

        Returns:
            dict: A dictionary with object IDs as keys and object
            instances as values.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets an object in the storage.

        Args:
            obj: The object to store.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file __file_path.
        """
        odictObj = FileStorage.__objects
        objects_dict = {key: obj.to_dict() for key, obj in odictObj.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """
        Deserializes the JSON file __file_path to __objects if it exists.
        """
        try:
            with open(FileStorage.__file_path) as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(cls_name)(**value))
        except FileNotFoundError:
            pass
