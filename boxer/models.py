from __future__ import unicode_literals
from django.db import models
from mongoengine import *

class Applets(Document):
    icon_url = StringField()
    cid = StringField()
    content_name = StringField()
    placement_id = IntField()

class Content(Document):
    cid = StringField()
    title = StringField()
    description = StringField()
    url = StringField()
    image_url = StringField()
    category = StringField()

class Filters(Document):
    _filter = StringField()
    title = StringField()
    cid = StringField()
    description = StringField()
    image_url = StringField()
    url = StringField()









