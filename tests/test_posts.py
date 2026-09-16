import pytest
import requests
from config.config import BASE_URL
from jsonschema import validate
from schemas.post_schema import post_schema

def test_create_post(client):

    url = f"{BASE_URL}/posts"

    payload = {
    "title": "API Automation",
    "body": "Learning API automation using Python",
    "userId": 1
    }

    response = client.post(url,payload)
    assert response.status_code == 201
    post_data = response.json()
    validate(
        instance=post_data,
        schema=post_schema
    )
    assert post_data["userId"] == 1
    assert "id" in post_data
    assert post_data["title"] == "API Automation"

def test_update_post(client):
    url = f"{BASE_URL}/posts/1"
    patch_payload = {
        "title": "Updated API Automation"
    }
    response = client.patch(url,patch_payload)
    assert response.status_code == 200
    update_data = response.json()
    assert update_data["title"] == "Updated API Automation"

def test_replace_post(client):
    url = f"{BASE_URL}/posts/1"
    put_payload = {
        "id": 1,
        "title": "API Automation with Python",
        "body": "Updated complete post",
        "userId": 1
    }
    response = client.put(url,put_payload)
    assert response.status_code == 200
    put_data = response.json()
    assert put_data["title"] == "API Automation with Python"
    assert put_data["body"] == "Updated complete post"
    assert put_data["userId"] == 1

def test_delete_post(client):
    url = f"{BASE_URL}/posts/1"
    response = client.delete(url)
    assert response.status_code == 200





# ---- This is for testing purpose---

# @pytest.mark.parametrize(
#     "payload",
#     [
#         (
#            {"role" : "QA" , "experience" : 7},
#               "name is required"
#         ),
#         (
#           {"name" : "Anudeep" , "experience" : 7},
#               "role is required"
#         ),
#         (
#           {"name" : "Anudeep" , "experience" : "seven"},
#             "experience must be an integer"
#         )
#
#     ]
# )
# def test_invalid_employee(client,payload,expected_error):
#     url = f"{BASE_URL}/employees"
#     response = client.post(url,payload)
#     assert response.status_code == 200
#     res_data = response.json()
#     assert res_data["error"] == "expected_error"
