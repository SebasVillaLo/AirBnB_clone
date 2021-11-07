#!/usr/bin/python3
"""
Class BaseModel
"""
import uuid
import datetime
import models

timeformat = "%Y-%m-%dT%H:%M:%S.%f"
class BaseModel:
    """code"""

    def __init__(self, *args, **kwargs):
        """init"""
        if kwargs:
            kwargs["created_at"] = datetime.datetime.strptime(
                kwargs["created_at"], timeformat)
            kwargs["updated_at"] = datetime.datetime.strptime(
                kwargs["updated_at"], timeformat)

            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """str"""
        return "[{}] ({}) <{}>".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """dict"""
        dictionarynew = {}
        dictionarynew = self.__dict__.copy()
        dictionarynew['__class__'] = self.__class__.__name__
        dictionarynew["created_at"] = self.created_at.isoformat()
        dictionarynew["updated_at"] = self.updated_at.isoformat()

        return dictionarynew
