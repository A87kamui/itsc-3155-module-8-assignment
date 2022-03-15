# TODO: Feature 2
import pytest
from flask.testing import FlaskClient


# refeer to app.py in root directory
def test_create_movie(test_app: FlaskClient):
    data = {
        'title': 'The Matrix',
        'director': 'Wachowski',
        'rating': 5
    }
    response = test_app.post('/movies', data=data)
    response_data = response.data
    assert b'<td>The Matrix</td>' in response_data