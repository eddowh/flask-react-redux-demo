# -*- coding: utf-8 -*-

from collections import OrderedDict

from restaurants.constants import CENTS_PER_DOLLAR


def serialize_menu_item(menu_item):
    return OrderedDict([
        ("id", menu_item.id),
        ("restaurant_id", menu_item.restaurant.id),
        ("name", menu_item.name),
        ("price", "{:.2f}".format(menu_item.price / float(CENTS_PER_DOLLAR))),
        ("course", menu_item.course),
        ("description", menu_item.description),
    ])


def serialize_restaurant(restaurant):
    return OrderedDict([
        ("id", restaurant.id),
        ("name", restaurant.name),
        ("menu_items", [
            serialize_menu_item(menu_item)
            for menu_item in restaurant.menuitems.all()
        ]),
    ])
