import requests
from resources.generate_user_data import generate_fake_user
import logging

def test_create_user_with_token(access_token):
    """This test creates a user using acces token which comes from conftest file,
    and verifies that user is created"""
    logger = logging.getLogger(__name__)
    url = "https://gorest.co.in/public/v2/users"
    data = generate_fake_user()   # we are using faker to create a fake user and hit this api.
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.post(url, headers=headers, json=data)
    user_id = response.json()["id"]
    assert response.status_code == 201
    return user_id


