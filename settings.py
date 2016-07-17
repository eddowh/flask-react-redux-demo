# -*- coding: utf-8 -*-

import os

from dotenv import load_dotenv
from sqlalchemy.engine.url import URL

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(BASE_DIR, 'api')

DOTENV_PATH = os.path.join(BASE_DIR, '.env')
load_dotenv(DOTENV_PATH)

INSTALLED_APPS = [
    'restaurants',
]

DATABASES = {
    'DEFAULT': {
        'ENGINE': os.environ.get('DBENGINE'),
        'NAME': os.environ.get('DBNAME'),
        'HOST': os.environ.get('DBHOST'),
        'PORT': os.environ.get('DBPORT'),
        'USER': os.environ.get('DBUSER'),
        'PASSWORD': os.environ.get('DBPWD'),
        'URI': os.environ.get('DBURI'),
    },
}

if DATABASES['DEFAULT'].get('URI'):
    DB_URI = DATABASES['DEFAULT'].get('URI')
else:
    DB_URI = str(URL(
        DATABASES['DEFAULT'].get('ENGINE'),
        username=DATABASES['DEFAULT'].get('USER'),
        password=DATABASES['DEFAULT'].get('PASSWORD'),
        host=DATABASES['DEFAULT'].get('HOST'),
        port=DATABASES['DEFAULT'].get('PORT'),
        database=DATABASES['DEFAULT'].get('NAME'),
    ))

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True
