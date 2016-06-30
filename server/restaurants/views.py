# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify

from restaurants.models import Restaurant

bp = Blueprint('restaurants', __name__)


def get_restaurant_context(restaurant):
    return {
        "id": restaurant.id,
        "name": restaurant.name,
    }


@bp.route('/', methods=['GET'])
def restaurant_index():
    restaurants = Restaurant.query.all()
    return jsonify([
        get_restaurant_context(restaurant)
        for restaurant in restaurants
    ])
