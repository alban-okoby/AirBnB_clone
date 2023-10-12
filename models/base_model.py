#!/usr/bin/python3
"""Define a Base class for all models"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Constructor for the BaseModel class.

        Initializes instance attributes, 'id', 'created_at', and
        'updated_at' based on the given 'kwargs' or generates
        them if 'kwargs' is empty.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value,
                        '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation of the BaseModel instance

        Returns a formatted string containing the class name, ID, and
        a dictionary of instance attributes.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convert the BaseModel instance to a dictionary.

        Returns a dictionary containing all instance attributes, including
        'created_at' and 'updated_at' in ISO format.
        """
        obj_dict = {
            'my_number': (type(self.my_number), self.my_number),
            'name': (type(self.name), self.name),
            '__class__': (type(self).__name__, self.__class__.__name__),
            'updated_at': (type(self.updated_at).__name__,
                self.updated_at.isoformat()),
            'id': (type(self.id).__name__, self.id),
            'created_at': (type(self.created_at).__name__,
                self.created_at.isoformat())
        }
        return obj_dict
