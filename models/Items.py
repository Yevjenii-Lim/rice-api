import sqlite3

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from db import db

cart = [
    {
      "title": "Калифорния в кунжуте с крабом ",
      "price": 92,
      "desc": "Нежный сыр, огурец с мясом нежного краба...",
      "id": 1
    },
    {
       "title": "Дакота",
       "price": 145,
       "desc": "Лосось, уsгорь, креветка, авокадо, яп майонез, икра тобико, икра лососьВес: 265 грамм.",
       "id": 2
    }
]

class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    desc = db.Column(db.String(300))
    type = db.Column(db.String(80))

    def __init__(self, title, price, desc, type):
        self.title = title
        self.price = price
        self.desc = desc
        self.type = type

    @classmethod
    def get_all_items(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {"id": self.id, "title": self.title, "price": self.price, "desc": self.desc, "type": self.type}
