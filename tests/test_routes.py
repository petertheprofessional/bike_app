from fastapi.testclient import TestClient

from bikes_app.main import app


def test_when_requesting_nonexistent_client_return_404():
    client = TestClient(app)
    response = client.get('/client/NONEXISTENTID')

    assert response.status_code == 404


def test_when_requesting_an_existent_client_return_200():
    client = TestClient(app)
    response = client.get('/client/C1')

    assert response.status_code == 200