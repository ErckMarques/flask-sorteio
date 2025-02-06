import pytest

from flask import Flask, current_app

@pytest.fixture()
# def app() -> Flask:
#     return 

@pytest.fixture()
def app_ctx(app: Flask):
    with app.app_context:
        yield

# para utilizar este acessório uitlize o decorador "@pytest.mark.usefixture('app_ctx')" e escreva a funcao de test