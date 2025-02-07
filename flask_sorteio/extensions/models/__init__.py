from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_sorteio.extensions.models import models # noqa

db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)