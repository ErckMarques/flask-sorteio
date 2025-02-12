from pathlib import Path
from flask import abort, Blueprint, render_template

bp = Blueprint('home', __name__)

@bp.route('/')
def report():
    return abort(404)