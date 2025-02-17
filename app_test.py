"""Unit test for Flask application."""
from app import app


client = app.test_client()


def test_read_main():
    """Returns Hello, World."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello World!"
