import pytest
import mongomock
from unittest.mock import patch


@pytest.fixture(autouse=True)
def mock_mongo():
    client = mongomock.MongoClient()
    with patch("src.database.get_client", return_value=client):
        with patch("src.database.get_database", return_value=client["jovemmatch_test"]):
            yield client
