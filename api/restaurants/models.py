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


class MenuItem(db.Model):
    __tablename__ = 'restaurants_menuitem'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    # store number of cents
    price = db.Column(db.Integer, nullable=False)
    course = db.Column(db.String(250))
    restaurant_id = db.Column(db.Integer,
                              db.ForeignKey('restaurants_restaurant.id'))

    restaurant = db.relationship(
        'Restaurant',
        backref=db.backref('menuitems', lazy='dynamic')
    )

    def __init__(self, name, price, restaurant, course="", description=""):
        self.name = name
        self.price = price
        self.course = course
        self.description = description
        self.restaurant = restaurant

    def __repr__(self):
        return '<MenuItem ({})>'.format(self.name)
