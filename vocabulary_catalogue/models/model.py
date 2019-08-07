from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    added_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, author):
        self.title = title
        self.author = author

class BookSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    author = fields.String(required=True)
    added_on = fields.DateTime(allow_none=True)
    abstract = fields.String(load_only=True)
    char_limit = fields.Integer(load_only=True)


class Vocab(db.Model):
    __tablename__ = 'vocabularies'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50), nullable=False)
    count = db.Column(db.Integer)
    added_on = db.Column(db.DateTime, default=datetime.utcnow)
    book_id = db.Column(db.ForeignKey(Book.id, ondelete='CASCADE'), nullable=False)

    def __init__(self, word, count, book_id):
        self.word = word
        self.count = count
        self.book_id = book_id


class VocabSchema(Schema):
    id = fields.Integer(dump_only=True)
    word = fields.String(required=True)
    count = fields.Integer(dump_only=True)
    book_id = fields.Integer(dump_only=True)
    added_on = fields.DateTime(allow_none=True)
