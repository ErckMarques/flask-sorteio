from flask import Flask

from .blueprints.home import bp as home_bp

def create_app():
    """Uma fábrica para a aplicação flask"""
    app = Flask(__name__)
    
    app.register_blueprint(home_bp)
    
    return app 

if __name__ == '__main__':
    app = create_app()

    with app.app_context():
        app.run(debug=True)