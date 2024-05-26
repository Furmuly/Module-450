import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from name_suggestions import suggest_names


def test_suggest_names():
    assert len(suggest_names("A")) <= 5
    assert "Alice" in suggest_names("A")
    assert "Bob" not in suggest_names("Z")
