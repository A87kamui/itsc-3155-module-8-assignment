# TODO: Feature 2
import pytest



@pytest.fixture(scope='module')


def test_create_movie(client):
    response = client.post('/movies', data=dict(title='Matrix', director='Wachowski', rating='5'))
    # test to see if the response is a redirect to the list all movies page
    assert response.location == 'http://localhost/movies'
