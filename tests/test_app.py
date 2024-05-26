import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index_page(client):
    rv = client.get("/")
    assert rv.status_code == 200


def test_name_suggestions(client):
    rv = client.post("/", data=dict(name_input='A'))
    assert b"Alice" in rv.data

    rv = client.post("/", data=dict(name_input='Z'))
    assert b"Bob" not in rv.data
