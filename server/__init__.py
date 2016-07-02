# -*- coding: utf-8 -*-

from importlib import import_module

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_script import Manager

import settings

from sqlalch import db


app = Flask(__name__)
app.config.from_object(settings)

# allow cross-origin
CORS(app)

# flask-sqlalchemy
db.init_app(app)

# flask-migrate
migrate = Migrate(app, db)
manager = Manager(app)

# installed applications
for installed_app in settings.INSTALLED_APPS:
    mod = import_module(installed_app)
    try:
        url_prefix = mod.URL_PREFIX
    except AttributeError:
        app.register_blueprint(mod.bp)
    else:
        app.register_blueprint(mod.bp,
                               url_prefix='/{}'.format(url_prefix))
