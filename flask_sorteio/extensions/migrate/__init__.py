from flask import Flask
from flask_migrate import Migrate

from flask_sorteio.extensions.models import db

migrate = Migrate()

def init_app(app: Flask):
    migrate.init_app(app, db)
