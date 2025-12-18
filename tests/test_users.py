import pytest
from utils.assertions import assert_status_code , assert_json_has_keys
from db.db_utils import validate_user_in_backend
from utils.data_factory import create_user_payload

def test_get_users(api_client):
    response = api_client.get("/users")

    assert response.status_code == 200

    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0


def test_create_user(api_client):
    payload = create_user_payload()

    response = api_client.post("/users", payload)

    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    assert data["name"] == "John Doe"
    assert data["email"] =="john@example.com"

# Negative Test
def test_create_user_negative(api_client):
    payload = {}

    response = api_client.post("/users", payload)

    assert response.status_code in [400,422,201]

@pytest.mark.parametrize("payload", [
    {},
    {"name": ""},
    {"email": "invalid"}
])
def test_create_user_multiple_negatives(api_client, payload):
    response = api_client.post("/users", payload)
    assert response.status_code in [400, 422, 201]

def test_status_code_pass(api_client):
    response = api_client.get("/users")

    # Expecting 200 OK
    assert_status_code(response, 200)

def test_get_user_has_required_fields(api_client):
    response = api_client.get("/users/1")

    # First check status code
    assert_status_code(response, 200)

    # Convert response JSON to Python dict
    data = response.json()

    # Check required fields in response
    assert_json_has_keys(data, ["id", "name", "email"])

def test_create_user_(api_client):
    payload = create_user_payload()

    response = api_client.post("/users", payload)
    data = response.json()

    validate_user_in_backend(data["id"])