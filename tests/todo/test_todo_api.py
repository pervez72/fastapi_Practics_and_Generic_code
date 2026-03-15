import pytest
from fastapi.testclient import TestClient
from app.auth.models import Users
from app.auth.dependency import get_current_user
from app.main import app


# --- Override get_current_user for tests ---
def override_get_current_user():
    return Users(id=1, username="testuser", email="test@test.com")


app.dependency_overrides[get_current_user] = override_get_current_user



# /todo/create
def test_create_todo(client: TestClient):
    todo_data = {
        "title": "Test Todo",
        "description": "Testing API todo",
        "priority": 1,
        "completed" : True
    }

    response = client.post("/todo/create", json=todo_data)
    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Test Todo"
    assert data["description"] == "Testing API todo"
    assert data["priority"] == 1
    assert data["completed"] == True



# /todo/get_todo
def test_get_user_todo(client: TestClient):
    response = client.get("/todo/get_todo")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)