from datetime import datetime

from mongoengine import *


class BaseModel(Document):
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }

    created_at = DateTimeField(
        default=datetime.now
    )

    updated_at = DateTimeField(
        default=datetime.now
    )

    @property
    def id_str(self):
        return str(self.id)

    @property
    def created_at_str(self):
        return self.created_at.strftime('%Y-%m-%d')

    @property
    def updated_at_str(self):
        return self.updated_at.strftime('%Y-%m-%d')



