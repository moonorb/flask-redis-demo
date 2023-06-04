import pytest
from flask import Flask

@pytest.fixture
def app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello, World!'

    return app

def test_index(app):
    client = app.test_client()

    response = client.get('/')
    assert response.status_code == 200

