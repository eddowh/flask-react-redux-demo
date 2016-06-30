# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(BASE_DIR, 'server')

INSTALLED_APPS = [
    'restaurants',
]

DATABASES = {
    'DEFAULT': {
        'URI': 'sqlite:///' + os.path.join(BASE_DIR, 'restaurantmenu.db'),
    },
}

SQLALCHEMY_DATABASE_URI = DATABASES['DEFAULT']['URI']
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True
