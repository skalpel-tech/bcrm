# coding: utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :

import datetime
import uuid
import json
from app.core.db import db

entity_schema = {
    "type": "object",
    "properties": {
        "entity_type_id": {"type": "string"},
        "content": {"type": "object"},
    },
    "required": [ "entity_type_id", "content" ],
}

entity_type_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "schema": {"type": "object"},
    },
    "required": [ "name", "schema" ],
}

class EntityType(db.Model):
    """ **EntityType** db model """

    __tablename__ = 'entity_type'

    id = db.Column(
        db.String(length=60),
        unique=True,
        nullable=False,
        primary_key=True
    )

    name = db.Column(
        db.String(length=80),
        unique=True,
        nullable=False,
        default=''
    )

    schema = db.Column(
        db.Text(),
        nullable=False
    )

    def __init__(self, **kwargs):
        self.id = uuid.uuid4().__str__()
        self.name = kwargs.get('name')
        self.schema = json.dumps(kwargs.get('schema'))

    def toDict(self):
        data = dict([])
        data['id'] = self.id
        data['name'] = self.name
        data['schema'] = json.loads(self.schema)
        return data


class Entity(db.Model):
    """ **EntityType** db model """

    __tablename__ = 'entity'

    id = db.Column(
        db.String(length=60),
        unique=True,
        nullable=False,
        primary_key=True,
    )

    entityTypeId = db.Column(
        db.String(length=60),
        db.ForeignKey('entity_type.id'),
        nullable=False
    )

    content = db.Column(
        db.Text(),
        nullable=False
    )

    def __init__(self, **kwargs):
        self.id = uuid.uuid4().__str__()
        self.entityTypeId = kwargs.get('entity_type_id')
        self.content = json.dumps(kwargs.get('content'))

    def toDict(self):
        data = dict([])
        data['id'] = self.id
        data['entity_type_id'] = self.entityTypeId
        data['content'] = json.loads(self.content)
        return data
