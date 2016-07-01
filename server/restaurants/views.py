# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request, url_for, Response

from restaurants.constants import CENTS_PER_DOLLAR
from restaurants.models import Restaurant, MenuItem
from restaurants.utils import serialize_menu_item, serialize_restaurant
from sqlalch import db

bp = Blueprint('restaurants', __name__)


@bp.route('/', methods=['GET'])
def restaurants_index():
    restaurants = Restaurant.query.all()
    return jsonify([
        serialize_restaurant(restaurant)
        for restaurant in restaurants
    ])


@bp.route('/<int:restaurant_id>/', methods=['GET'])
def restaurant_detail(restaurant_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first_or_404()
    return jsonify(
        serialize_restaurant(restaurant)
    )


@bp.route('/<int:restaurant_id>/newmenuitem/', methods=['POST'])
def new_restaurant_menu_item(restaurant_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first_or_404()
    data = request.get_json()

    name = data.get('name')
    price = data.get('price') * CENTS_PER_DOLLAR  # convert cents to dollars

    if name and price > 0:
        new_menuitem = MenuItem(
            name=name,
            price=round(price),  # ensure whole numbers for cents
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


@bp.route('/<int:restaurant_id>/<int:menu_id>/', methods=['GET'])
def menu_item_detail(restaurant_id, menu_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first_or_404()
    menu_item = restaurant.menuitems.filter_by(id=menu_id).first_or_404()

    return jsonify(serialize_menu_item(menu_item))


@bp.route('/<int:restaurant_id>/<int:menu_id>/edit/', methods=['POST'])
def edit_menu_item(restaurant_id, menu_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first_or_404()
    menu_item = restaurant.menuitems.filter_by(id=menu_id).first_or_404()
    data = request.get_json()
    is_modified = False

    for field in ['name', 'course', 'description']:
        new_data = data.get(field)
        if new_data and new_data != getattr(menu_item, field):
            setattr(menu_item, field, new_data)
            is_modified = True

    new_price = round(data.get('price') * CENTS_PER_DOLLAR)
    if new_price > 0:
        if new_price != menu_item.price:
            menu_item.price = new_price
            is_modified = True
    else:
        return '', 400

    if is_modified:
        db.session.commit()
    return Response(
        status='201',
        headers={
            'Location': url_for('restaurants.menu_item_detail',
                                restaurant_id=restaurant.id,
                                menu_id=menu_item.id),
        }
    )


@bp.route('/<int:restaurant_id>/<int:menu_id>/delete/', methods=['POST'])
def delete_menu_item(restaurant_id, menu_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first_or_404()
    menu_item = restaurant.menuitems.filter_by(id=menu_id).first_or_404()

    db.session.delete(menu_item)
    db.session.commit()
    return Response(
        status='204',
        headers={
            'Location': url_for('restaurants.restaurant_detail',
                                restaurant_id=restaurant.id),
        }
    )
