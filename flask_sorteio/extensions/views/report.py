from flask import Blueprint, render_template

bp = Blueprint('report', __name__)

@bp.route('/relatorio')
def index():
    return render_template('relatorio/index.html')