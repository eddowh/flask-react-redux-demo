# -*- coding: utf-8 -*-


from importlib import import_module
import sys

from flask_migrate import MigrateCommand

import settings

sys.path.insert(1, settings.BASE_DIR)
sys.path.insert(1, settings.APP_DIR)

server = import_module('server')
manager = server.manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
