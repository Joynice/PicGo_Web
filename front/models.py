# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
from exts import db
from shortuuid import uuid
import datetime

class Images(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.String(50), primary_key=True, default=uuid)
    name = db.Column(db.String(500), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
    link = db.Column(db.String(500), nullable=False)
    type = db.Column(db.String(50))