"""Adiciona a extensão Flask DebugToobar para desenvolvimento"""

from flask_debugtoolbar import DebugToolbarExtension, Flask

def init_app(app: Flask):
    if app.config.get('SECRET_KEY') is None:
        app.config['SECRET_KEY'] = '342db8e7dadfc5ef81ef696382b40fba9cad65abcf475234878be8661b09784e'
    if app.config.get('DEBUG'):
        DebugToolbarExtension(app)
        