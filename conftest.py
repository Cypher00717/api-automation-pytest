import pytest   
from api.client.user_client import AuthClient
from Utils.config import base_url
from api.endpoints import login_user_endpoint
from data.test_data import registerPayload

@pytest.fixture
def api_client():
    return AuthClient(base_url, None)

@pytest.fixture
def auth_client(api_client):
    response = api_client.post(login_user_endpoint, registerPayload)
    token = response.json().get("token")

    return AuthClient(base_url, token)


