# -*- coding: utf-8 -*-

import subprocess

from server import app, db

db.create_all(app=app)
subprocess.check_output(['python', 'manage.py', 'db', 'init'])
