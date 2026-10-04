from data.test_data import registerPayload, invalid_payload, missing_email, missing_password, empty_payload
from api.endpoints import login_user_endpoint, auth_me_endpoint, register_user_endpoint, get_event_endpoint
from Utils.schema_validator import validate_schema
import pytest
import json
from jsonschema import validate



@pytest.mark.sanity
def test_register_user(api_client):
    response = api_client.post(register_user_endpoint, registerPayload)
    assert response.status_code in [201, 400] # Assuming 201 for successful registration and 400 for already registered user


@pytest.mark.login
def test_login_user(api_client):
    response = api_client.post(login_user_endpoint, registerPayload)
    assert response.status_code == 200

@pytest.mark.auth_me
def test_auth_me(auth_client):
    response = auth_client.get(auth_me_endpoint)
    body = response.json()

    validate_schema(body, 'schemas/auth_me.json')

    assert response.status_code == 200
    assert "userId" in body["user"], "userId not found in response"
    assert "email" in body["user"], "email not found in response"
    assert body["user"]["email"] == registerPayload["email"], "Email does not match the registered email"


@pytest.mark.negative
def test_invalid_login_user(api_client):
    response = api_client.post(login_user_endpoint, invalid_payload)
    assert response.status_code == 400
    body = response.json()
    assert body["success"] is False, "Expected success to be False for invalid login"
    assert body["error"] == "Invalid email or password", "Expected error message for invalid login"


@pytest.mark.missing
def test_missing_fields_login_user(api_client):
    
    response = api_client.post(login_user_endpoint, missing_email)
    assert response.status_code == 400
    body = response.json()

    validate_schema(body, 'schemas/login_error_schema.json')

    assert body["success"] is False, "Expected success to be False for missing fields login"
    assert body["error"] == "Validation failed", "Expected error message for missing fields login"
    #assert body["details"][0]["field"] == "email", "Expected missing field to be 'email'"
    #assert body["details"][0]["message"] == "Email is required", "Expected error message for missing email"


@pytest.mark.get_event
def test_get_event(auth_client):
    response = auth_client.get(get_event_endpoint)
    assert response.status_code == 404
    body = response.json()
    assert body["success"] is False, "Expected success to be False for get event"
    assert body["error"] == "Event with id 1 not found", "Expected error message for get event"
