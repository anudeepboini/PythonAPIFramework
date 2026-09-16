import pytest
from utils.api_client import APIClient

@pytest.fixture
def client():
    return APIClient()
