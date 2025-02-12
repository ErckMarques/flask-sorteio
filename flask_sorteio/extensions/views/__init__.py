from flask import Flask

from .report import bp as report_bp
from .home import bp as home_bp

def init_app(app: Flask):
    app.register_blueprint(home_bp)
    app.register_blueprint(report_bp)