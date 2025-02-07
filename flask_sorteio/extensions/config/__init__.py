"""Gerencia as configurações da aplicação"""
from pathlib import Path

from flask import Flask
from dynaconf import FlaskDynaconf

def init_app(app: Flask):
    # FlaskDynaconf(app, settings_files=['settings.toml'])
    app.logger.info('Iniciando as configurações da aplicação')
    # app.config.load(Path(__file__).absolute().parents[3].joinpath('settings.toml'))
    FlaskDynaconf(app, settings_files=[Path(__file__).absolute().parents[3].joinpath('settings.toml')])


