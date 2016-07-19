####################################
Flask, SQLAlchemy, and React.js Demo
####################################

Installation
============

Project Dependencies
--------------------

.. code:: sh

    $ npm install --progress
    $ pip install -r requirements-dev.txt


Running Locally
===============

Local Configuration File
------------------------

You'll need to configure and register several variables that should not be exposed publicly. This will be done in ``.env``; see `.env.example <./.env.example>`_) for a guide on how to set it up.

Do not proceed to the next section until you have done so.

Migrate Database
----------------

You'll have to first create your database, using any of the `databases supported by SQLAlchemy <http://docs.sqlalchemy.org/en/latest/core/engines.html>`_.

Following that, run the database migrations:

.. code:: sh

    $ python manage.py db upgrade

Run the Backend Server
----------------------

.. code:: sh

    $ python manage.py runserver

Visit the application at http://localhost:5000 (the port is set to 5000 by default).

For more options, consult ``python manage.py runserver --help``.

Run the Frontend Server
-----------------------

The backend API must be running before you start the React app.

.. code:: sh

    $ npm run dev

Visit the application at http://localhost:3000 (the port is set to 3000 by default).

For more options, consult ``webpack-dev-server --help``.

Licensing
=========
See `LICENSE <./LICENSE>`_.


:Authors:
    Eddo Williams Hintoso
