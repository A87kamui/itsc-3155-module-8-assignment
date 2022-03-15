# TODO: Feature 2
import pytest
from flask.testing import FlaskClient


# refeer to app.py in root directory
def test_create_movie(test_app: FlaskClient):
    # data = {
    #     'title': 'The Matrix',
    #     'director': 'Wachowski',
    #     'rating': 5
    # }
    response = test_app.get('/movies/new')
    response_data = response.data
    assert b'<h1 class="mb-5">Create Movie Rating</h1>' in response_data
    assert b'<p class="mb-3">Create a movie rating below</p>' in response_data