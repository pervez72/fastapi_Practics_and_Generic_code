import pytest
from fastapi import HTTPException
from app.auth.servics import create_user, authenticate_user, login_user, get_user_by_id

# --- Fixture for test user data ---
@pytest.fixture
def user_data():
    return {
        "username": "testuser",
        "email": "test@test.com",
        "password": "1234",
        "phone_number": "01711111111"
    }


def test_create_user(db_session, user_data):
    user = create_user(
        db=db_session,
        username=user_data["username"],
        email=user_data["email"],
        password=user_data["password"],
        phone_number=user_data["phone_number"]
    )

    assert user.id is not None
    assert user.username == user_data["username"]
    assert user.email == user_data["email"]
    assert user.hashed_password != user_data["password"]  # Ensure password is hashed


def test_create_user_duplicate(db_session, user_data):
    # Duplicate email should raise HTTPException
    with pytest.raises(HTTPException):
        create_user(
            db=db_session,
            username="anotheruser",
            email=user_data["email"],
            password="5678",
            phone_number="01722222222"
        )


def test_authenticate_user(db_session, user_data):
    # Correct login
    user = authenticate_user(db_session, email=user_data["email"], password=user_data["password"])
    assert user is not None
    assert user.email == user_data["email"]

    # Wrong password
    assert authenticate_user(db_session, email=user_data["email"], password="wrong") is None

    # Non-existing user
    assert authenticate_user(db_session, email="nouser@test.com", password="1234") is None


def test_login_user(db_session, user_data):
    res = login_user(db_session, email=user_data["email"], password=user_data["password"])
    assert "access_token" in res
    assert res["token_type"] == "bearer"

    # Invalid login
    with pytest.raises(HTTPException):
        login_user(db_session, email=user_data["email"], password="wrong")



def test_get_user_by_id(db_session):
    # Step 1: create a fresh user
    user = create_user(
        db=db_session,
        username="getuser",
        email="getuser@test.com",
        password="1234",
        phone_number="01733333333"
    )

    # Step 2: fetch by ID
    fetched_user = get_user_by_id(db_session, user_id=user.id)
    assert fetched_user is not None
    assert fetched_user.email == "getuser@test.com"

    # Step 3: non-existing user
    assert get_user_by_id(db_session, user_id=9999) is None