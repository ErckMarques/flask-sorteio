from flask import Flask

from flask_sorteio.extensions.blueprints.home import bp as home_bp
from flask_sorteio.extensions import toobar

def create_app():
    """Uma fábrica para a aplicação flask"""
    app = Flask(__name__)
    
    toobar.init_app(app)
    
    app.register_blueprint(home_bp)
    
    return app 

if __name__ == '__main__':
    app = create_app()

    with app.app_context():
        app.run(debug=True)