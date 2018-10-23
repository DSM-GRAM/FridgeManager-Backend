from mongoengine import *


class SampleM(Document):
    id = StringField(primary_key=True)
    pw = StringField(required=True, max_length=8)
