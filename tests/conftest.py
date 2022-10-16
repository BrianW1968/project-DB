from fastapi.testclient import TestClient
from main import app
import schemas
import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database import get_db
from database import Base
import pytest
from oauth2 import create_access_token

SQLALCHEMY_DATABASE_URL = f'postgresql://{config.settings.database_username}:{config.settings.database_password}@{config.settings.database_hostname}:{config.settings.database_port}/{config.settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

client = TestClient(app)

@pytest.fixture(scope="module")
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db=TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def client(session):
    def overrid_get_db():
    
        try:
          yield session
        finally:
          session.close()
    app.dependency_overrides[get_db] = overrid_get_db
    yield TestClient(app)

@pytest.fixture(scope="module")
def test_user(client):
    user_data = {"email": "brianawalsh@gmail.com", "password": "password1234"}
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201
    print(res.json())
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user

@pytest.fixture
def token(test_user):
    create_access_token({"user_id": test_user['id']})

@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

