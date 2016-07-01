# -*- coding: utf-8 -*-

from collections import OrderedDict

from flask import Blueprint, jsonify, request, url_for, Response

from restaurants.models import Restaurant, MenuItem
from sqlalch import db

bp = Blueprint('restaurants', __name__)


def get_menu_item_context(menu_item):
    return OrderedDict([
        ("id", menu_item.id),
        ("restaurant_id", menu_item.restaurant.id),
        ("name", menu_item.name),
        ("price", "{:.2f}".format(menu_item.price)),
        ("course", menu_item.course),
        ("description", menu_item.description),
    ])


def get_restaurant_context(restaurant):
    return OrderedDict([
        ("id", restaurant.id),
        ("name", restaurant.name),
        ("menu_items", [
            get_menu_item_context(menu_item)
            for menu_item in restaurant.menuitems.all()
        ]),
    ])


@bp.route('/', methods=['GET'])
def restaurants_index():
    restaurants = Restaurant.query.all()
    return jsonify([
        get_restaurant_context(restaurant)
        for restaurant in restaurants
    ])


@bp.route('/<int:restaurant_id>', methods=['GET'])
def restaurant_detail(restaurant_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first_or_404()
    return jsonify(
        get_restaurant_context(restaurant)
    )


@bp.route('/<int:restaurant_id>/newmenuitem/', methods=['POST'])
def new_restaurant_menu_item(restaurant_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first_or_404()
    data = request.get_json()

    name = data.get('name')
    price = data.get('price')

    if name and price > 0:
        new_menuitem = MenuItem(
            name=name, price=price,
            restaurant=restaurant,
            course=data.get('course', ''),
            description=data.get('description', '')
        )
        db.session.add(new_menuitem)
        db.session.commit()
        return Response(
            status='201',
            headers={
                'Location': url_for('restaurants.restaurant_detail',
                                    restaurant_id=restaurant.id),
            }
        )
    else:
        return '', 400
