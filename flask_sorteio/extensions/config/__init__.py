"""Gerencia as configurações da aplicação"""
from pathlib import Path

from flask import Flask

def init_app(app: Flask):
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{Path(__file__).absolute().parents[4].joinpath('db/sorteio_flask.sqlite')}"

