import pytest
from unittest.mock import patch
from name_suggestions import suggest_names

names_database = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]


def test_suggest_names():
    assert len(suggest_names("A", names_database)) <= 5
    assert "Alice" in suggest_names("A", names_database)
    assert "Bob" not in suggest_names("Z", names_database)


@patch('name_suggestions.generate_random_name')
def test_generate_names_with_mock(mock_generate_random_name):
    # Mocking the generate_random_name function to return a controlled name
    mock_generate_random_name.return_value = "MockName"

    from name_suggestions import generate_names_database
    database = generate_names_database(10)

    assert all(name == "MockName" for name in database)
