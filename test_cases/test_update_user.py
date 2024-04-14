import requests
from test_create_new_user import test_create_user_with_token

def test_update_user(access_token):
    """This test case verifies that the user's name is updated correctly through a PATCH request."""
    user_id = test_create_user_with_token(access_token) #id of user that will be updated
    
    # Test case to update user
    url = f"https://gorest.co.in/public/v2/users/{user_id}"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    data = {
        "name": "sachin_shukla"    #name of that user will be updated
    }
    response = requests.patch(url, headers=headers, json=data)
    user_name_from_response = response.json()['name']
    given_user_name = data["name"]
    assert user_name_from_response == given_user_name # here we are verifying that name in the response is same as given name