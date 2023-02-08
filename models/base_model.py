#!/usr/bin/python3
"""Base Model Module
This module is in charge of establishing a reference
Base Model for the rest of the classes of the
Airbnb Clone project
"""
from datetime import datetime
import models
import uuid

class BaseModel
"""
This is the Base Model that take care of the
initialization, serialization and deserialization
of the future instances.
"""


    def __init__(self, *args, **kwargs):
        """Base Model __init__ Method
        Here, the default values of a Base Model
        instance are initialized.
        """
        if kwargs:
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')

                if arg != '__class__':
                    setattr(self, arg, val)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = self.created_at
                    models.storage.new(self)


     def __str__(self):
             """
             This method prints the content of the Base Model
            class with this format
            $ [<class name>] (<self.id>) <self.__dict__>
             """
             return '[{0}] ({1}) {2}'.format(
                 self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
             """
             Updates the public instance attribute `updated_at`
             with the current datetime and dumps the class data
             into a file
             """
             self.updated_at = datetime.now()
             models.storage.save()


    def to_dict()self:
            """
            onverts the information of the class to human-readable format
            Returns a new dictionary containing all keys/values
            of __dict__ of the instance.
            """
             class_info = self.__dict__.copy()
             class_info['__class__'] = self.__class__.__name__
             class_info['created_at'] = self.created_at.isoformat()
             class_info['updated_at'] = self.updated_at.isoformat()

             return class_info
