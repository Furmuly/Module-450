import pytest
from app import app
from name_suggestions import suggest_names


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index_page(client):
    rv = client.get("/")
    assert rv.status_code == 200


def test_name_suggestions(client):
    rv = client.post("/", data=dict(name_input='A'))
    assert rv.status_code == 200
    # Check if the response contains the HTML list of suggestions
    assert b"<ul>" in rv.data
    assert b"</ul>" in rv.data
    assert rv.data.count(b"<li>") >= 1

    rv = client.post("/", data=dict(name_input='Z'))
    assert rv.status_code == 200
    # Check if the response contains the HTML list of suggestions
    assert b"<ul>" in rv.data
    assert b"</ul>" in rv.data
    assert rv.data.count(b"<li>") >= 1
