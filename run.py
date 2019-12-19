# -*- coding: UTF-8 -*-
__author__ = 'Joynice'

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from front import front_bp
import config
from exts import db


def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect()
    csrf.init_app(app=app)
    app.config.from_object(config.config)
    app.register_blueprint(front_bp)
    db.init_app(app=app)
    return app

app = create_app()

if __name__ == '__main__':
    app.run()