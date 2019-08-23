# coding: utf-8
from sqlalchemy import Column, Integer, Table, Text
from sqlalchemy.sql.sqltypes import NullType
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Chat(db.Model):
    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    writer_id = db.Column(db.Integer, nullable=False)
    w_time = db.Column(db.Text, nullable=False)
    url_id = db.Column(db.Integer, nullable=False)


t_sqlite_sequence = db.Table(
    'sqlite_sequence',
    db.Column('name', db.NullType),
    db.Column('seq', db.NullType)

)
