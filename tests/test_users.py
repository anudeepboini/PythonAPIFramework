import pytest
import requests
from config.config import BASE_URL
from jsonschema import validate
from schemas.post_schema import post_schema

def test_get_user(client):
    url = f"{BASE_URL}/users/1"
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"

@pytest.mark.parametrize(
    "user_id",
    [ 9998,
      8569,
      5236
      ]
)
def test_user_not_found(client, user_id):
    url = f"{BASE_URL}/users/{user_id}"
    response = client.get(url)
    assert response.status_code == 404