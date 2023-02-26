from setup_db import db
from marshmallow import Schema, fields
class Genre(db.Model):
    __tablename__ = 'genre.py'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
