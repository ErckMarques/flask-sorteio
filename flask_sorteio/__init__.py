from flask import Flask

from flask_sorteio.extensions import views
from flask_sorteio.extensions import toobar

def create_app():
    """Uma fábrica para a aplicação flask"""
    app = Flask(__name__)
    
    # inicializa as extensões
    
    # inicializa a extensão flask_debug_toobar para debug
    toobar.init_app(app)
    
    # registra os blueprints na aplicação
    views.init_app(app)
    
    return app 

if __name__ == '__main__':
    app = create_app()

    with app.app_context():
        app.run(debug=True)