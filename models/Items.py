import sqlite3

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from db import db


class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    desc = db.Column(db.String(300))
    type = db.Column(db.String(80))
    img = db.Column(db.String())
    amount = db.Column(db.Integer())

    def __init__(self, title, price, desc, type, img, amount):
        self.title = title
        self.price = price
        self.desc = desc
        self.type = type
        self.img = img
        self.amount = amount

    @classmethod
    def get_all_items(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {"id": self.id, "title": self.title, "price": self.price, "desc": self.desc, "type": self.type, "img": self.img, "amount": self.amount }
