# -*- coding: utf-8 -*-

from flask import Flask
import settings

app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"
