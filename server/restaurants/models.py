# -*- coding: utf-8 -*-

from sqlalch import db


class Restaurant(db.Model):
    __tablename__ = 'restaurants_restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Restaurant ({})>'.format(self.name)
