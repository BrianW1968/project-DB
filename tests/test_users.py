import schemas
import pytest
from jose import jwt
from config import settings




#@pytest.fixture

def test_create_user(client):
    res = client.post("/users/", json={"email":"hello1234@gmail.com", "password": "password123"})
    print(res.json())
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello1234@gmail.com"
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post(
        "/login", data={"username": test_user['email'], "password":test_user['password']}
    )
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

def test_incorrect_login(client, test_user):
    res = client.post("/login", data={"username": test_user["email"], "password": "wrongPassword"})

    assert res.status_code == 403
    assert res.json().get('detail') == 'Invalid Credentials'