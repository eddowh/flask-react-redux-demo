# -*- coding: utf-8 -*-

from importlib import import_module

from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate

import settings

from sqlalch import db


app = Flask(__name__)
app.config.from_object(settings)

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
