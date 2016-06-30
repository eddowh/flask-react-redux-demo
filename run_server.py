# -*- coding: utf-8 -*-

import sys

from server import app
import settings

sys.path.insert(1, settings.BASE_DIR)
sys.path.insert(1, settings.APP_DIR)


if __name__ == '__main__':
    app.debug = settings.DEBUG
    app.run(
        host=settings.HOST,
        port=settings.PORT
    )
