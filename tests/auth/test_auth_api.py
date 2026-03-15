import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.auth.models import Users
from app.auth.dependency import get_current_user
import uuid

# --- Override current_user dependency ---
def override_get_current_user():
    return Users(id=1, username="testuser", email="test@test.com")

app.dependency_overrides[get_current_user] = override_get_current_user


@pytest.fixture
def test_user():
    # Unique email per test run → prevents duplicate conflicts
    unique_email = f"apitest_{uuid.uuid4().hex[:6]}@test.com"
    return {
        "username": "apitestuser",
        "email": unique_email,
        "password": "1234",
        "phone_number": "01711111111"
    }


def test_register_user(client: TestClient, test_user):
    response = client.put("/auth/register", json=test_user)
    assert response.status_code == 200

    data = response.json()
    assert data["username"] == test_user["username"]
    assert data["email"] == test_user["email"]
    assert "hashed_password" in data


def test_register_duplicate_user(client: TestClient):
    # Create a user first
    user_data = {
        "username": "dupuser",
        "email": "dupuser@test.com",
        "password": "1234",
        "phone_number": "01722222222"
    }
    client.put("/auth/register", json=user_data)

    # Duplicate registration should fail
    response = client.put("/auth/register", json=user_data)
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Users All Ready Registered"


def test_login_user(client: TestClient):
    # Create user first
    user_data = {
        "username": "loginuser",
        "email": "loginuser@test.com",
        "password": "1234",
        "phone_number": "01733333333"
    }
    client.put("/auth/register", json=user_data)

    # login using OAuth2PasswordRequestForm fields (username=email)
    login_data = {
        "username": user_data["email"],
        "password": user_data["password"]
    }
    response = client.post("/auth/login", data=login_data)
    assert response.status_code == 200

    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_password(client: TestClient):
    # Create user first
    user_data = {
        "username": "wrongpassuser",
        "email": "wrongpass@test.com",
        "password": "1234",
        "phone_number": "01744444444"
    }
    client.put("/auth/register", json=user_data)

    # Try login with wrong password
    login_data = {
        "username": user_data["email"],
        "password": "wrongpassword"
    }
    response = client.post("/auth/login", data=login_data)
    assert response.status_code == 401
    data = response.json()
    assert data["detail"] == "Invalid email or password"