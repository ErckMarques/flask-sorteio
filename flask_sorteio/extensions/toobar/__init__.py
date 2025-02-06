"""Adiciona a extensão Flask DebugToobar para desenvolvimento"""

from flask_debugtoolbar import DebugToolbarExtension, Flask

def init_app(app: Flask):
    if app.config.get('DEBUG'):
        DebugToolbarExtension(app)
        