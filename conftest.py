from app import create_app, socketio
import pytest

app = create_app()

@pytest.fixture
def api():
    client = app.test_client()
    return client

@pytest.fixture
def sock():
    client = socketio.test_client(app)
    return client
