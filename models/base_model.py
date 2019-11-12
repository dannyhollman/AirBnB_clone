#!/usr/bin/python3
"""Base class for all classes"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """base class"""
    _count = 0

    def __init__(self, *args, **kwargs):
        """init base class"""
        if len(kwargs) > 0:
            type(self)._count += 1
            self.__dict__.update(**kwargs)
            self.created_at = datetime.strptime(self.created_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
        else:
            type(self)._count += 1
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """return string representation"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, dict(self.__dict__))

    def save(self):
        """save update"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """convert to dictionary"""
        dic = dict(self.__dict__)
        dic.update(__class__=self.__class__.__name__)
        dic["created_at"] = dic["created_at"].isoformat()
        dic["updated_at"] = dic["updated_at"].isoformat()
        return dic
