"""Gerencia as configurações da aplicação"""
from pathlib import Path

from flask import Flask
from dynaconf import FlaskDynaconf

def init_app(app: Flask):
    FlaskDynaconf(app, settings_files=['settings.toml'])
    


