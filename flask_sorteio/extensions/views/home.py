from pathlib import Path
from flask import Blueprint, current_app, render_template

bp = Blueprint('home', __name__)

@bp.route('/')
def report():
    return render_template('relatorio/index.html')